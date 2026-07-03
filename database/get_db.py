import pymysql
from .config import DB, DB_without_database

def get_db_database_connection():
    return pymysql.connect(
        host = DB_without_database['host'],
        user = DB_without_database['user'],
        password = DB_without_database['password'],
        cursorclass = pymysql.cursors.DictCursor,
        autocommit = True
    )

def get_db():
    return pymysql.connect(
        host = DB['host'],
        user = DB['user'],
        password = DB['password'],
        database = DB['database'],
        cursorclass = pymysql.cursors.DictCursor,
        autocommit = True
    )