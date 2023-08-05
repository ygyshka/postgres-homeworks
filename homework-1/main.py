"""Скрипт для заполнения данными таблиц в БД Postgres."""
import datetime

import psycopg2
import csv


CUSTOMERS_PATH = 'north_data/customers_data.csv'
EMPLOYERS_PATH = 'north_data/employees_data.csv'
ORDERS_PATH = 'north_data/orders_data.csv'


def insert_table_customers(list_data):
    conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='2112')

    try:
        with conn:
            # create cursor
            with conn.cursor() as cur:
                # execute query
                for row in list_data:
                    cur.execute('insert into customers values (%s, %s, %s)', (row[0], row[1], row[2]))
    finally:
        conn.close()


def insert_table_employers(list_data):
    conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='2112')

    try:
        with conn:
            # create cursor
            with conn.cursor() as cur:
                # execute query
                for row in list_data:
                    cur.execute('insert into employers values (%s, %s, %s, %s, %s, %s)',
                                (row[0], row[1], row[2], row[3], row[4], row[5]))
    finally:
        conn.close()


def insert_table_orders(list_data):
    conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='2112')

    try:
        with conn:
            # create cursor
            with conn.cursor() as cur:
                # execute query
                for row in list_data:
                    cur.execute('insert into orders values (%s, %s, %s, %s, %s)',
                                (row[0], row[1], row[2], row[3], row[4]))
    finally:
        conn.close()


def read_csv(path):
    with open(path, 'r', encoding='UTF-8') as f:
        reader = csv.reader(f)
        list_ = []
        for row in reader:
            list_.append(row)
    return list_


if __name__ == "__main__":
    list_customers = read_csv(CUSTOMERS_PATH)[1:]
    list_employers = read_csv(EMPLOYERS_PATH)[1:]
    list_orders = read_csv(ORDERS_PATH)[1:]
    insert_table_customers(list_customers)
    insert_table_employers(list_employers)
    insert_table_orders(list_orders)

