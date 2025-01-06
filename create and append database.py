import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn=sqlite3.connect(db_file)
        print(sqlite3.version)
        print(sqlite3.sqlite_version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

if __name__=='__main__':
    create_connection(r"C:\Users\henry\OneDrive\Documents\GitHub\python_football_data_analysis.db")


    