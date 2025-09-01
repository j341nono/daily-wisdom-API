import sqlite3
import json
from typing import List, Tuple
import argparse


SAVE_PATH: str = "data/data.json"

DB_NAME: str = "src/database/data.db"

TABLE_NAME: str = "quotes_table"

CREATE_TABLE_TEXT: str = f"""CREATE TABLE IF NOT EXISTS {TABLE_NAME} (" \
"id INTEGER PRIMARY KEY AUTOINCREMENT," \
"philosopher STRING," \
"quotes STRING)"""

INSERT_TABLE_TEXT: str = f"INSERT INTO {TABLE_NAME} (philosopher, quotes) VALUES (?, ?)"
DELETE_TABLE_TEXT: str = f"DELETE FROM {TABLE_NAME} where philosopher = ? AND quotes = ?"


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--initial_commit", action="store_true")
    parser.add_argument("--philosopher", type=str, help="Philosopher's name")
    parser.add_argument("--quotes", type=str, help="Quote text")
    parser.add_argument("--delete", action="store_true")
    return parser.parse_args()


def create_table() -> None:
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute(CREATE_TABLE_TEXT)
    conn.commit()
    conn.close()


def insert_qoute(philosopher: str, quotes: str) -> None:
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute(INSERT_TABLE_TEXT, (philosopher, quotes))
    conn.commit()
    conn.close()


def insert_many(quotes: List[Tuple[str, str]]) -> None:
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.executemany(INSERT_TABLE_TEXT, quotes)
    conn.commit()
    conn.close()


def delete_qoute(philosopher: str, quotes: str) -> int:
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute(DELETE_TABLE_TEXT, (philosopher, quotes))
    conn.commit()
    delete_rows = cur.rowcount
    conn.close()
    return delete_rows


def prepare_json_for_db(save_path: str) -> List[Tuple[str, str]]:
    with open(save_path, "r", encoding="utf-8") as f:
        data_list: List[dict[Tuple[str, list]]] = json.load(f)
    
    input_list: List[Tuple[str, str]] = []
    for data_line in data_list:
        philosopher = data_line.get("philosopher")
        quotes_list = data_line.get("quotes")
        for quote in quotes_list:
            input_list.append((philosopher, quote))
    return input_list 


def initial_commit() -> None:
    input_list: List[Tuple[str, str]] = prepare_json_for_db(save_path=SAVE_PATH)
    insert_many(quotes=input_list)


def main():
    args = parse_args()
    if (args.philosopher and not args.quotes) or (args.quotes and not args.philosopher):
        print("--philosopher と --quotes はセットで指定してください。")

    create_table()

    if args.initial_commit:
        initial_commit()
    elif args.delete:
        delete_qoute(philosopher=args.philosopher, quotes=args.quotes)
    elif args.philosopher and args.quotes:
        insert_qoute(philosopher=args.philosopher, quotes=args.quotes)


def debug_insert_table():
    philosopher = "john"
    quotes = "you can do it."
    insert_qoute(philosopher=philosopher, quotes=quotes)


def debug_insert_many():
    input_list: List[Tuple[str, str]] = prepare_json_for_db(save_path=SAVE_PATH)
    insert_many(quotes=input_list)
    

if __name__ == "__main__":
    # create_table()
    # debug_insert_table()
    main()
