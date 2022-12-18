import os
import glob
from sqlite3 import Timestamp
from typing import List
import json
from datetime import datetime
import psycopg2

from airflow.hooks.postgres_hook import PostgresHook

from airflow import DAG
from airflow.utils import timezone
from airflow.operators.python import PythonOperator


# cat ~/.aws/credentials
aws_access_key_id = 'ASIAWUFIZZORVKLYYOPX'
aws_secret_access_key = 'gFch7TCjha/Ife7llQ1iJCfqF4iL2UiwYHnYtO5O'
aws_session_token = 'FwoGZXIvYXdzEBoaDBB/sInsJ1d2dXZ6yyLUAQ79TZwLhNvU/o5VEWkxXV5Zz56omH3tMDzFGqOkeTP3QV2MlyJSKQI2g9u1VtUzE0d3kOP9nhPpx0zDL4n5UoHsXMteAlhzK6lZhCUsXsOdT1mlHnGqB8E2UPH6X/YPzbna/7kc7ayA9gr0xgMTZpC6UDptDWzXvefcmXVkJRIbILHx0sbUNy3qFYrUwzQhY77oaezRViIDXmHdAWd1Zcz2Ib+dU4MwxcWKcxbE94Lp3Ml4qKYHtn3wELtY7k8KTte3YxCnssyOQE6WdOXcua8pywBXKMGp+5wGMi0+GRGzWj67+l61iYj4hPS9nTmgeOxzr2i0iRAt8zTn970UOUmAdypPVlih0Ug'


def _create_tables():

    hook = PostgresHook(postgres_conn_id="my-redshift")
    conn = hook.get_conn()
    cur = conn.cursor()

    create_table_queries = [
        """
       DROP TABLE IF EXISTS customer_val
        """,
        """
        CREATE TABLE IF NOT EXISTS customer_val (
            Row_ID	bigint
            ,Order_ID text	
            ,Order_Date	date
            ,Ship_Date date
            ,Ship_Mode text	
            ,Customer_ID text	
            ,Customer_Name text	
            ,Segment text	
            ,Country text	
            ,City text	
            ,State text	
            ,Postal_Code text	
            ,Region text	
            ,Product_ID text	
            ,Category text	
            ,Sub_Category text	
            ,Product_Name text	
            ,Sales decimal	
            ,Quantity bigint	
            ,Discount decimal	
            ,Profit decimal
        )
        """,
        """
       DROP TABLE IF EXISTS customer
        """,
        """
        CREATE TABLE IF NOT EXISTS customer (
            Row_id bigint,
            Order_id text,
            Order_date date,
            Customer_id text,
            Customer_name text,
            City text,
            Postal_code text,
            Region text,
            Product_id text,
            Category text,
            Sub_category text,
            Sales decimal,
            Quantity int,
            Discount decimal,
            Profit decimal
        )
        """
    ]

    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def _load_staging_tables():

    hook = PostgresHook(postgres_conn_id="my-redshift")
    conn = hook.get_conn()
    cur = conn.cursor()

    copy_table_queries = [
        """
        COPY customer_val
        FROM 's3://preawcapstone/Superstoresale.csv'
        ACCESS_KEY_ID '{0}'
        SECRET_ACCESS_KEY '{1}'
        SESSION_TOKEN '{2}'
        CSV
        DELIMITER ','
        DATEFORMAT 'MM/DD/YYYY'
        ACCEPTINVCHARS 
        IGNOREHEADER 1
        """
    ]

    for query in copy_table_queries:
        cur.execute(query.format(aws_access_key_id, aws_secret_access_key, aws_session_token))
        conn.commit()


def _insert_dwh_tables():

    hook = PostgresHook(postgres_conn_id="my-redshift")
    conn = hook.get_conn()
    cur = conn.cursor()

    insert_dwh_queries = [
    """
    INSERT INTO customer
    SELECT Row_id ,
            Order_id ,
            Order_date ,
            Customer_id ,
            Customer_name ,
            City ,
            Postal_code ,
            Region ,
            Product_id ,
            Category ,
            Sub_category ,
            Sales ,
            Quantity ,
            Discount ,
            Profit 
    FROM customer_val
    
    """,
]
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

    load_staging_tables = PythonOperator(
       task_id = 'load_staging_tables',
       python_callable = _load_staging_tables,
    )

    insert_dwh_tables = PythonOperator(
       task_id = 'insert_dwh_tables',
       python_callable = _insert_dwh_tables,
    )

    create_tables >> load_staging_tables >> insert_dwh_tables