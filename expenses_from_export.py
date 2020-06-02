def load_expenses():
    """ Выгрузка из файла расходов по датам и категориям."""
    filename = 'export.csv'
    expense_list = []

    with open(filename) as f_obj:
        rows = f_obj.readlines()
        for row in rows:
            if "Expense" in row:
                expense_list.append(row)
    for expense in expense_list:
        expense = expense.split('","')
        amount = expense[5]
        category = expense[3]
        date = expense[0]
        date = date[1:]
        print(date, category, amount)
