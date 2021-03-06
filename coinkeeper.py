import psycopg2

from datetime import timedelta, datetime

conn = psycopg2.connect(database="coinkeeper", user="postgres", password="postgres", host="localhost", port=5432)


def load_expenses():
    """Загрузка данных из базы."""

    expenses = []
    with conn.cursor() as cur:
        cur.execute("SELECT e.amount, c.name, e.date FROM expense e JOIN category c on e.category_id = c.id")
        row_tuple = cur.fetchone()

        while row_tuple:
            row_dict = {"amount": row_tuple[0], "category": row_tuple[1], "date": row_tuple[2]}
            expenses.append(row_dict)
            row_tuple = cur.fetchone()
    return expenses


def add_expense():
    """Добавление расхода."""

    with conn.cursor() as cur:
        cur.execute("SELECT id, name FROM category")
        category = cur.fetchall()

    print(category)


    msg = input('Please enter category id: ')
    category_id = int(msg)
    msg = input('Please enter expense amount: ')
    amount = float(msg)
    msg = input('Please enter date: ')
    date = msg

    # sql = "INSERT INTO expense (amount, category_id, date) VALUES (" + str(amount) + ', ' + str(category_id) + ", '" + date + "' )"
    sql = f"INSERT INTO expense (amount, category_id, date) VALUES ({amount}, {category_id}, '{date}')"

    with conn.cursor() as cur:
        cur.execute(sql)
    conn.commit()


def show_expenses():
    """Просмотр расходов."""
    expenses = load_expenses()
    total_amount = 0
    for expense in expenses:
        total_amount += expense['amount']
        print(expense)
    print(f'Total: {total_amount:.2f}')


def total_between_dates():
    """Сумма расходов между двумя датами по категориям."""
    msg_1 = input('Please enter first date (default 30 days ago):')
    first_date =    msg_1
    if first_date == '':
        first_date = datetime.now() - timedelta(days=30)
        first_date = first_date.replace(hour=0, minute=0, second=0,microsecond=0)
    msg_2 = input('Please enter second date (default now):')
    second_date = msg_2
    if second_date == '':
        second_date = datetime.now()
    sql = f"""SELECT e.amount, c.name, e.date FROM expense e JOIN category c on e.category_id = c.id 
            WHERE e.date BETWEEN %s AND %s """

    with conn.cursor() as cur:
        cur.execute(sql, [first_date, second_date])
        expenses_between_dates = cur.fetchall()

    sum_total = 0
    sum_by_category = {}

    for amount, name, date in expenses_between_dates:
        sum_total = sum_total + amount
        if name not in sum_by_category:
            sum_by_category[name] = 0
        sum_by_category[name] = sum_by_category[name] + amount
    print('Sum by category: ', sum_by_category)
    print('Total: ', sum_total)


def show_main_menu():
    """Показ главного меню."""
    while True:
        choice = input(
            "Main menu:\n"
            "1. Add record\n"
            "2. Print all records\n"
            "3. Print between dates\n"
            "q. Quit\n> ")
        if choice == str(1):
            add_expense()
        elif choice == str(2):
            show_expenses()
        elif choice == str(3):
            total_between_dates()
        elif choice == 'q':
            print('Thank you for using Coinkeeper!')
            break
        else:
            print('Please choose a number:')
            continue


if __name__ == '__main__':
    show_main_menu()
