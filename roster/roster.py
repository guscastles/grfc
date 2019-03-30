# coding: utf-8
"""
Fruit Roster Creator

Script for the fruit roster, using SQLite. The DB file is *fruit_roster.db*.
"""
from contextlib import contextmanager
from sqlite3 import connect
import pandas as pd


NAMES_AND_DATES = [('Tatiana', '2019-03-23'),
                   ('Alison', '2019-03-30'),
                   ('Sara', '2019-04-06'),
                   ('Kylie', '2019-04-13'),
                   ('Julie', '2019-04-20'),
                   ('Lyndal', '2019-04-27'),
                   ('Hege', '2019-05-04'),
                   ('Tina', '2019-05-11'),
                   ('Tasmeen', '2019-05-18'),
                   ('Tatiana', '2019-05-25'),
                   ('Alison', '2019-06-01'),
                   ('Sara', '2019-06-08'),
                   ('Kylie', '2019-06-15'),
                   ('Julie', '2019-06-22'),
                   ('Lyndal', '2019-06-29'),
                   ('Hege', '2019-07-06'),
                   ('Tina', '2019-07-13'),
                   ('Tasmeen', '2019-07-20'),
                   ]
"""Initial names and dates when creating the *fruit_roster.db* file,
a SQLite database."""


def create_database():
    """Creates the database"""
    with connect("fruit_roster.db") as conn:
        cur = conn.cursor()
        cur.execute("create table roster (id integer primary key, name text, date text)")


def insert_new_records(new_records):
    """Inserts new records in the fruit roster database."""
    with _database_cursor() as cursor:
        _insert_records(new_records, cursor)


def select_all_records():
    """Select all records from the fruit roster"""
    with _database_cursor() as cursor:
        return cursor.execute('select * from roster').fetchall()


@contextmanager
def _database_cursor(isolation_level=None):
    """Returns the cursor to the database."""
    conn = connect("fruit_roster.db", isolation_level=isolation_level)
    yield conn.cursor()
    conn.close()


def _insert_records(records, cursor):
    """Receives a list for record containing names and dates
    and a cursor to the database. Inserts the records into the
    database.
    """
    insert = "insert into roster values(NULL, '{}', '{}')"
    for name, date in records:
        cursor.execute(insert.format(name, date))


def generate_report(raw_data):
    """Generates the report for the whole season."""
    dataframe = pd.DataFrame(raw_data)
    names_and_dates = dataframe.rename({1: "Name", 2: "Date"}, axis=1).drop(0, axis=1)
    names_and_dates["Date"] = pd.to_datetime(names_and_dates["Date"], yearfirst=True)
    names_and_dates.rename({num: num + 1 for num in range(18)}, axis=0, inplace=True)
    names_and_dates.to_html(open("roster.html", "w"),
                            formatters={"Date": lambda dt: pd.datetime.strftime(dt, "%d/%m/%Y")},
                            justify="left")
