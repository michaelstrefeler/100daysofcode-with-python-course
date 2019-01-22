from contextlib import contextmanager
import sqlite3

name = ""


@contextmanager
def create_db(name):
    try:
        conn = sqlite3.connect(f'{name}.db')
        cursor = conn.cursor()
        yield cursor
    finally:
        conn.close()


def prompt_for_name():
    name = input("What would you like to name your test db file?: ")
    return name


def get_table_name():
    table_name = input("What would you liek to name your table?: ")
    table_name.replace(' ', '_')
    return table_name


if __name__ == "__main__":
    name = prompt_for_name()
    table_name = get_table_name()
    with create_db(name) as cursor:
        cursor.execute(f"""CREATE TABLE {table_name}
    (col1 TEXT, col2 TEXT, col3 TEXT, col4 INT)""")
    print(f'{name}.db has been created')
    print(f'The table {table_name} has also been created')
