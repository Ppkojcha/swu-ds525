import os
import glob
from sqlite3 import Timestamp
from typing import List
import json
from datetime import datetime
import psycopg2

from airflow import DAG
from airflow.utils import timezone
from airflow.operators.python import PythonOperator
# from airflow.operators.bash_operator import BashOperator
# from airflow.hooks.postgres_hook import PostgresHook

curr_date = datetime.today().strftime('%Y-%m-%d')


create_table_queries = [
    """
    CREATE TABLE IF NOT EXISTS Customer (
        Customer_id bigint,
        Order_id int,
        Order_date datetime,
        Customer_name text,
        City text,
        Postal_code text,
        Region text,

    )
    """,
    """
    CREATE TABLE IF NOT EXISTS Product (
        Product_id text,
        Category text,
        Sub_category text,
        Customer_id bigint
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS Sales (
        Customer_id bigint,
        Sales float64,
        Quantity int,
        Discount float64,
        Profit float64
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS Customer_value (
        Customer_id bigint,
        Order_id int,
        Order_date datetime,
        Customer_name text,
        City text,
        Postal_code text,
        Region text,
        Product_id text

    )
    """
    

]

truncate_table_queries = [
    """
    TRUNCATE TABLE Customer
    """,
    """
    TRUNCATE TABLE Product
    """,
    """
    TRUNCATE TABLE Sales
    """,
    """
    TRUNCATE TABLE Customer_value
    """,
]

# cat ~/.aws/credentials
# https://stackoverflow.com/questions/15261743/how-to-copy-csv-data-file-to-amazon-redshift
aws_access_key_id = ''
aws_secret_access_key = ''
aws_session_token = ''

copy_table_queries = [
    """
    COPY Customer 
    FROM 's3://jaochin-dataset-fifa/cleaned/leagues/date_oprt={0}'
    ACCESS_KEY_ID '{1}'
    SECRET_ACCESS_KEY '{2}'
    SESSION_TOKEN '{3}'
    CSV
    DELIMITER ','
    IGNOREHEADER 1
    """,
    """
    COPY Product 
    FROM 's3://jaochin-dataset-fifa/cleaned/clubs/date_oprt={0}'
    ACCESS_KEY_ID '{1}'
    SECRET_ACCESS_KEY '{2}'
    SESSION_TOKEN '{3}'
    CSV
    DELIMITER ','
    IGNOREHEADER 1
    """,
    """
    COPY Sales 
    FROM 's3://jaochin-dataset-fifa/cleaned/nationalities/date_oprt={0}'
    ACCESS_KEY_ID '{1}'
    SECRET_ACCESS_KEY '{2}'
    SESSION_TOKEN '{3}'
    CSV
    DELIMITER ','
    IGNOREHEADER 1
    """,
]

clear_dwh_queries = [
    """
    DELETE FROM player_value_wage WHERE date_oprt = current_date
    """,
]

insert_dwh_queries = [
    """
    INSERT INTO player_value_wage 
    SELECT p.player_id
        , p.player_name
        , p.player_age 
        , p.player_overall 
        , p.player_value 
        , p.player_wage 
        , pos.position_name 
        , c.club_name 
        , n.nationality_name 
        , l.league_name 
        , current_date
    FROM players p
    INNER JOIN positions pos
        ON pos.position_id = p.position_id
    INNER JOIN nationalities n
        ON n.nationality_id = p.nationality_id
    INNER JOIN clubs c
        ON c.club_id = p.club_id
    INNER JOIN leagues l
        ON l.league_id = c.league_id
    """,
]

host = "redshift-cluster-1.c7om6vv9mbp9.us-east-1.redshift.amazonaws.com"
port = "5439"
dbname = "dev"
user = "awsuser"
password = "awsPassword1"
conn_str = f"host={host} dbname={dbname} user={user} password={password} port={port}"
conn = psycopg2.connect(conn_str)
cur = conn.cursor()

def _create_tables():
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()

def _truncate_datalake_tables():
    for query in truncate_table_queries:
        cur.execute(query)
        conn.commit()

def _load_staging_tables():
    for query in copy_table_queries:
        cur.execute(query.format(curr_date, aws_access_key_id, aws_secret_access_key, aws_session_token))
        conn.commit()

def _clear_dwh_tables():
    for query in clear_dwh_queries:
        cur.execute(query)
        conn.commit()

def _insert_dwh_tables():
    for query in insert_dwh_queries:
        cur.execute(query)
        conn.commit()


with DAG(
    'Capstone',
    start_date = timezone.datetime(2022, 12, 1), # Start of the flow
    schedule = '@monthly', # Run once a month at midnight of the first day of the month
    tags = ['capstone'],
    catchup = False, # No need to catchup the missing run since start_date
) as dag:


    create_tables = PythonOperator(
        task_id = 'create_tables',
        python_callable = _create_tables,
    )

    truncate_datalake_tables = PythonOperator(
        task_id = 'truncate_datalake_tables',
        python_callable = _truncate_datalake_tables,
    )

    load_staging_tables = PythonOperator(
        task_id = 'load_staging_tables',
        python_callable = _load_staging_tables,
    )

    clear_dwh_tables = PythonOperator(
        task_id = 'clear_dwh_tables',
        python_callable = _clear_dwh_tables,
    )

    insert_dwh_tables = PythonOperator(
        task_id = 'insert_dwh_tables',
        python_callable = _insert_dwh_tables,
    )

    create_tables >> truncate_datalake_tables >> load_staging_tables >> clear_dwh_tables >> insert_dwh_tables