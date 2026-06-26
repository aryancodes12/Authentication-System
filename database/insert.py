import pymysql
from .get_db import get_db

def insert_user(name, username, email, password):
    try:
        conn = cursor = None
        conn = get_db()
        cursor = conn.cursor()

        query = """INSERT INTO users (name, username, email, password)
                VALUES(%s, %s, %s, %s)"""
        
        values = (name, username, email, password)
        cursor.execute(query, values)
    
    except pymysql.MySQLError as e:
        print(f"\nError: {e}\n")

    finally:
        if cursor: cursor.close()
        if conn: conn.close()
