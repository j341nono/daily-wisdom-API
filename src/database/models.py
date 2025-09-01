import sqlite3

SAVE_PATH: str = "data/data.json"

DB_NAME = "data.db"

def main():
    conn = sqlite3.connect(DB_NAME)
    conn.close()

if __name__ == "__main__":
    main()
