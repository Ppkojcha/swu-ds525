from cassandra.cluster import Cluster
import glob
import json
import os
from typing import List

import psycopg2


#Drop table 

table_drop_actor = "DROP TABLE IF EXISTS Actor"
table_drop_event = "DROP TABLE IF EXISTS Event"

#สร้างตาราง

table_create_actor = """
    CREATE TABLE IF NOT EXISTS Actor (
        id int,
        login varchar,
        display_login varchar,
        PRIMARY KEY ((id),login)
    )
"""

table_create_event = """
    CREATE TABLE IF NOT EXISTS Event (
        id bigint,
        type varchar ,
        create_at timestamp,
        PRIMARY KEY ((id),create_at)
        )
"""
create_table_queries = [
    table_create_actor,table_create_event
]
drop_table_queries = [
    table_drop_event,table_create_actor
]

#Fuction ดึงข้อมูลจาก .json 
def get_files(filepath: str) -> List[str]:
    """
    Description: This function is responsible for listing the files in a directory
    """

    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, "*.json"))
        for f in files:
            all_files.append(os.path.abspath(f))

    num_files = len(all_files)
    print(f"{num_files} files found in {filepath}")

    return all_files




def drop_tables(session):
    for query in drop_table_queries:
        try:
            rows = session.execute(query)
        except Exception as e:
            print(e)


def create_tables(session):
    for query in create_table_queries:
        try:
            session.execute(query)
        except Exception as e:
            print(e)


def process(session, filepath):
    # Get list of files from filepath
    all_files = get_files(filepath)

    for datafile in all_files:
        with open(datafile, "r") as f:
            data = json.loads(f.read())
            for each in data:
               
                 # Insert data into Actor table 
                
                try:
                    query_actor = "INSERT INTO Actor (id,login,display_login) \
                        VALUES (%s, '%s', '%s')" \
                        % (each["actor"]["id"], each["actor"]["login"], each["actor"]["display_login"])
                except:
                    query_actor = "INSERT INTO Actor (id,login,display_login) \
                        VALUES (%s, '%s', '%s')" \
                        % (each["actor"]["id"], each["actor"]["login"], each["actor"]["display_login"])
              
                    session.execute(query_actor)    

                try:
                    if each["payload"]["push_id"] != None :
                        query_event = "INSERT INTO Event (id,type,create_at) \
                            VALUES (%s, '%s', '%s')" \
                            % (each["id"], each["type"], each["created_at"])
                        session.execute(query_event)
                        
                    else :
                        query_event = "INSERT INTO Event (id,type,create_at) \
                            VALUES (%s, '%s', '%s')" \
                            % (each["id"], each["type"], each["created_at"])
                        session.execute(query_event)
                        
                except:
                    pass





def main():
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()

    # Create keyspace
    try:
        session.execute(
            """
            CREATE KEYSPACE IF NOT EXISTS github_events
            WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }
            """
        )
    except Exception as e:
        print(e)

    # Set keyspace
    try:
        session.set_keyspace("github_events")
    except Exception as e:
        print(e)

    drop_tables(session)
    create_tables(session)
    process(session, filepath="../data")
    #insert_sample_data(session)

    # Select data in Cassandra and print them to stdout
    query1 = """
    SELECT id,type,create_at from Event --WHERE public='True' ORDER BY created_at DESC
     """
    try:
        rows = session.execute(query1)
    except Exception as e:
        print(e)

    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
