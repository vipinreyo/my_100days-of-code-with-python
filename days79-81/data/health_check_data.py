import os
import sqlite3
from collections import namedtuple

HEALTH_DB = "health.db"
HealthData = namedtuple("HealthData", ('date', 'name', 'status', 'error_info'))


def create_db_and_initialize_table():
    conn = sqlite3.connect(HEALTH_DB)
    cur = conn.cursor()

    health_data_table = """CREATE TABLE IF NOT EXISTS health_data (
                            date text,
                            name text,
                            status text,
                            error_info text
                          );"""
    cur.execute(health_data_table)

    with conn:
        sql = "INSERT INTO health_data (date, name, status, error_info) values ('2018-09-20', 'CaLM', 'BAU', " \
              "'No Error')"
        cur.execute(sql)

        sql = "INSERT INTO health_data (date, name, status, error_info) values ('2018-09-21', 'GaaS', 'Not normal', " \
          "'No connection')"
        cur.execute(sql)


if not os.path.exists(HEALTH_DB):
    create_db_and_initialize_table()


def get_health_data():
    with sqlite3.connect(HEALTH_DB) as conn:
        cur = conn.cursor()
        sql = "SELECT * from health_data;"
        cur.execute(sql)

        result = []
        for row in cur.fetchall():
            result.append(row)

    return result
