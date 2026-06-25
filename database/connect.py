import pymysql
from db import get_db

try:
    conn = cursor = None
    conn = get_db()
    print(f"\nConnection Successfull!\n")

    cursor = conn.cursor()
except pymysql.MySQLError as e:
    print(f"\nError: {e}\n")