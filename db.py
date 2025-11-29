import pymysql
from config import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME

def get_connection():
    connection = pymysql.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True
    )
    return connection

def save_message(user_id: int, username: str | None, text: str):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = """
            INSERT INTO messages (user_id, username, text)
            VALUES (%s, %s, %s)
            """
            cursor.execute(sql, (user_id, username, text))
    finally:
        conn.close()

def get_last_messages(limit: int = 5):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = """
            SELECT user_id, username, text, created_at
            FROM messages
            ORDER BY id DESC
            LIMIT %s
            """
            cursor.execute(sql, (limit,))
            result = cursor.fetchall()
            return result
    finally:
        conn.close()
