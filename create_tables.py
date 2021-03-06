import psycopg2
from sql_queries import create_table_queries, drop_table_queries, database_drop, database_create


def create_database():
    """
    Used to delete pre-existing database to ensure that our database does not throw any error if we try creating a
    database that already exists. Then create a database called sparkifydb and connect to sparkifydb.
    :return: cur: database cursor
             conn: connection to studentdb database
    """
    # connect to default database
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    # create sparkify database with UTF8 encoding
    cur.execute(database_drop)
    cur.execute(database_create)

    # close connection to default database
    conn.close()    
    
    # connect to sparkify database
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()
    
    return cur, conn


def drop_tables(cur, conn):
    """
    Used to delete pre-existing table to ensure that our database does not throw any error if we try creating a
    table that already exists.
    :param cur: cursor;
    :param conn: connection;
    :return: None
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    Create tables based on the queries in create_table_queries list.
    :param cur: cursor;
    :param conn: connection; connection to studentdb database
    :return: None
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    cur, conn = create_database()
    
    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
