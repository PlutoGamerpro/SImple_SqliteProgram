import sqlite3


def user_exists(username):
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()

    cursor.execute("SELECT 1 FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()

    conn.close()

    return result is not None
