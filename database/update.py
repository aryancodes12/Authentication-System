import pymysql
from .get_db import get_db

#Update name of user
def update_user_name(old_name, new_name):
    try:
        conn = cursor = None
        conn = get_db()
        cursor = conn.cursor()

        query = "UPDATE users SET name = %s WHERE name = %s"
        cursor.execute(query, (new_name, old_name))
        
    except pymysql.MySQLError as e:
        print(e)
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


#Update password of user
def update_user_password(new_password, user_email):
    try:
        conn = cursor = None
        conn = get_db()
        cursor = conn.cursor()

        query = "UPDATE users SET password = %s WHERE email = %s"

        cursor.execute(query, (new_password, user_email),)

    except pymysql.MySQLError as e:
        print(e)
    finally:
        if cursor: cursor.close()
        if conn: conn.close()