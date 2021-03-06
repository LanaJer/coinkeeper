from datetime import date


def load_expenses_csv(filename ='export.csv'):
    """ Выгрузка из файла расходов по датам и категориям."""
    with open(filename) as f_obj:
        rows = f_obj.readlines()

    expenses_raw = []
    for row in rows:
        if "Expense" in row:
            expenses_raw.append(row)

    transformed_expenses = []
    for expense in expenses_raw:
        expense = expense.split('","')
        amount = expense[5]
        category = expense[3]
        d = expense[0][1:].split('/')
        expense_date = date(year=int(d[2]), month=int(d[0]),day=int(d[1]))
        item = [expense_date, category, amount]
        transformed_expenses.append(item)
    return transformed_expenses


if __name__ == '__main__':
    expense_list = load_expenses_csv()
    for d, c, a in expense_list:
        print(d, c, a)
