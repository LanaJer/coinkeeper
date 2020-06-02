import psycopg2

from datetime import timedelta, datetime

from expenses_from_export import load_expenses

conn = psycopg2.connect(database="coinkeeper", user="postgres", password="postgres", host="localhost", port=5432)


def import_to_database(expense_list):
    """Импорт данных в базу."""
    pass


if __name__ == '__main__':
    expense_list = load_expenses()
    import_to_database(expense_list)
