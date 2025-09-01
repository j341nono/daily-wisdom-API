import sqlite3

SAVE_PATH: str = "data/data.json"

DB_NAME = "src/database/data.db"

CREATE_TABLE_TEXT = "CREATE TABLE IF NOT EXISTS quotes_table (" \
"id INTEGER PRIMARY KEY AUTOINCREMENT," \
"philosopher STRING," \
"quotes STRING)"

INSERT_TABLE_TEXT = "INSERT INTO quotes_table (philosopher, quotes) VALUES (?, ?)"


def create_table():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute(CREATE_TABLE_TEXT)
    conn.commit()
    conn.close()


def insert_qoute(philosopher: str, quotes: str):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute(INSERT_TABLE_TEXT, (philosopher, quotes))
    conn.commit()
    conn.close()


def debug_insert_table():
    philosopher = "john"
    quotes = "you can do it."
    insert_qoute(philosopher=philosopher, quotes=quotes)


if __name__ == "__main__":
    create_table()
    debug_insert_table()
