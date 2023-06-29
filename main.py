from fastapi import FastAPI
from datetime import datetime
import sqlite3
from sqlite3 import Error, Connection
from typing import Tuple

app = FastAPI()
db_file = 'data.db'


def create_connection() -> Connection:
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn


def create_table(conn: Connection):
    sql_tasks = """
    CREATE TABLE IF NOT EXISTS iot1(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        light REAL NOT NULL,
        temperature REAL NOT NULL
    );
    """
    try:
        cursor = conn.cursor()
        cursor.execute(sql_tasks)
    except Error as e:
        print(e)


def insert_project(conn: Connection, project: Tuple[str, float, float]):
    sql = """
    INSERT INTO iot1(date, light, temperature)
    VALUES (?, ?, ?)
    """
    cursor = conn.cursor()
    cursor.execute(sql, project)
    conn.commit()


def select_all_tasks(conn: Connection, count:
