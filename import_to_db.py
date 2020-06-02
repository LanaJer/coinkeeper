import psycopg2

from datetime import timedelta, datetime

from load_expenses_csv import load_expenses_csv

conn = psycopg2.connect(database="coinkeeper", user="postgres", password="postgres", host="localhost", port=5432)


def import_to_database(expense_list):
    """Импорт данных в базу."""
    print('import', expense_list)


if __name__ == '__main__':
    expense_list = load_expenses_csv()
    import_to_database(expense_list)
