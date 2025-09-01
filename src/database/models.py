import sqlite3

SAVE_PATH: str = "data/data.json"

DB_NAME = "src/database/data.db"

CREATE_TABLE_TEXT = "CREATE TABLE IF NOT EXISTS quotes (" \
"id INTEGER PRIMARY KEY AUTOINCREMENT," \
"philosopher STRING," \
"quotes STRING)"


def create_table():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute(CREATE_TABLE_TEXT)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()
