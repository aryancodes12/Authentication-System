import pymysql
from config import DB

def get_db():
    return pymysql.connect(
        host = DB['host'],
        user = DB['user'],
        password = DB['password'],
        database = DB['database'],
        cursorclass = pymysql.cursors.DictCursor,
        autocommit = True
    )