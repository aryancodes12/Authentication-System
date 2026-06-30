import pymysql
from .get_db import get_db

#Fetching all users
def select_all_users():
    try:
        conn = cursor = None
        conn = get_db()
        cursor = conn.cursor()

        query = """SELECT * FROM users"""

        cursor.execute(query)

        users = cursor.fetchall()

        if not users:
            print(f"\nDatabase Empty\n")
        else:
            print(f"\nUsers in Database:\n")
            return users
        
    except pymysql.MySQLError as e:
        print(f"\nError: {e}\n")

    finally:
        if cursor: cursor.close()
        if conn: conn.close()

#SELECT only one user to maintain session
def select_one_user_info(username):
    try:
        conn = cursor = None
        conn = get_db()
        cursor = conn.cursor()

        query = """SELECT * FROM users WHERE username = %s"""

        cursor.execute(query, (username),)

        user_info = cursor.fetchone()
        
        return user_info
        
    except pymysql.MySQLError as e:
        print(f"\nError: {e}\n")

    finally:
        if cursor: cursor.close()
        if conn: conn.close()

#SELECTING USERNAME TO CHECK IF IT'S UNIQUE
def is_username_exists(username):
    try:
        conn = cursor = None
        conn = get_db()
        cursor = conn.cursor()

        query = "SELECT username FROM users WHERE username = %s"
        
        cursor.execute(query, (username),)
        row = cursor.fetchone()

        if row:
            return True
        return False
        
            
    except pymysql.MySQLError as e:
        print(e)
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


#Checking for duplicate email
def is_email_exists(email):
    try:
        conn = cursor = None
        conn = get_db()
        cursor = conn.cursor()

        query = "SELECT email FROM users WHERE email = %s"

        cursor.execute(query, (email),)
        row = cursor.fetchone()

        if row:
            return True
        return False
    
    except pymysql.MySQLError as e:
        print(e)
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

#Fetching to verify password entered by user
def is_correct_pass(username):
    try:
        conn = cursor = None
        conn = get_db()
        cursor = conn.cursor()

        query = "SELECT password FROM users WHERE username = %s"

        cursor.execute(query, (username),)
        row = cursor.fetchone()

        if row:
            return row
        return False
    
    except pymysql.MySQLError as e:
        print(e)
    finally:
        if cursor: cursor.close()
        if conn: conn.close()
