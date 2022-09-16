
import psycopg2



table_drop_events = "DROP TABLE IF EXISTS Events"
table_drop_actors = "DROP TABLE IF EXISTS Actors"
table_drop_repo = "DROP TABLE IF EXISTS Repo"


table_create_actors = """
    CREATE TABLE IF NOT EXISTS Actors (
        id int,
        login text,
        display_login text,
        PRIMARY KEY(id)
    )
"""
table_create_events = """
    CREATE TABLE IF NOT EXISTS Events (
        id text,
        type text,
        actor_id int,
        repo_id int,
        PRIMARY KEY(id),
        CONSTRAINT fk_actor FOREIGN KEY(actor_id) REFERENCES actors(id)

    )
"""
table_create_repo = """
    CREATE TABLE IF NOT EXISTS Repo (
        id int,
        name text,
        url text,
        PRIMARY KEY(id)
    )
"""

create_table_queries = [
    table_create_actors,
    table_create_events,
    table_create_repo,
    
]
drop_table_queries = [
    table_drop_events,
    table_drop_actors,
    table_drop_repo,
    
]


def drop_tables(cur, conn) -> None:
    """
    Drops each table using the queries in `drop_table_queries` list.
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn) -> None:
    """
    Creates each table using the queries in `create_table_queries` list.
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    - Drops (if exists) and Creates the sparkify database.
    - Establishes connection with the sparkify database and gets
    cursor to it.
    - Drops all the tables.
    - Creates all tables needed.
    - Finally, closes the connection.
    """
    conn = psycopg2.connect(
        "host=127.0.0.1 dbname=postgres user=postgres password=postgres"
    )
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
