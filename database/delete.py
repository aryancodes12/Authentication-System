import pymysql
from .get_db import get_db

#Delete user account
def delete_user(username):
    try:
        conn = cursor = None
        conn = get_db()
        cursor = conn.cursor()

        query = "DELETE FROM users WHERE username = %s"

        cursor.execute(query, (username),)

    except pymysql.MySQLError as e:
        print(e)
    finally:
        if cursor: cursor.close()
        if conn: conn.close()