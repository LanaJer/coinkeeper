import psycopg2

from datetime import timedelta, datetime

from load_expenses_csv import load_expenses_csv

conn = psycopg2.connect(database="coinkeeper", user="postgres", password="postgres", host="localhost", port=5432)


def import_to_database(expense_list):
    """Импорт данных в базу."""
    print('import', expense_list)
    for date, category, amount in expense_list:
        sql = f'SELECT id from category WHERE name = %s '
        with conn.cursor() as cur:
            cur.execute(sql, [category])
            row = cur.fetchone()
            if row:
                category_id = row[0]
            else:
                sql = 'INSERT INTO category (name) VALUES (%s) RETURNING id'
                cur.execute(sql, [category])
                row = cur.fetchone()
                category_id = row[0]
                print('new', category, category_id)

            sql = 'INSERT INTO expense (amount, category_id, date) VALUES (%s, %s, %s) '
            cur.execute(sql, [amount, category_id, date])
    conn.commit()



if __name__ == '__main__':
    expense_list = load_expenses_csv()
    import_to_database(expense_list)
