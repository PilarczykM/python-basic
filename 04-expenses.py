expenses = []


def show_expenses(month):
    for expense_amount, expense_type, expense_month in expenses:
        if expense_month == month:
            print(f'{expense_amount} - {expense_type}')


def add_expense(month):
    print()
    expense_amount = int(input("Enter the amount [zł]: "))
    expense_type = input("Enter the type of expense (food, entertainment, home, other): ")

    expense = (expense_amount, expense_type, month)
    expenses.append(expense)


def show_stats(month):
    total_amount_this_month = sum(
        expense_amount for expense_amount, _, expense_month in expenses if expense_month == month)
    number_of_expenses_this_month = sum(1 for _, _, expense_month in expenses if expense_month == month)
    average_expense_this_month = total_amount_this_month / number_of_expenses_this_month

    total_amount_all = sum(expense_amount for expense_amount, _, _ in expenses)
    average_expense_all = total_amount_all / len(expenses)

    print()
    print("Statistics")
    print("All expenses for this month [zł]:", total_amount_this_month)
    print("Average expenditure this month [zł]: ", average_expense_this_month)
    print("All expenses [zł]:", total_amount_all)
    print("Average expense [zł]: ", average_expense_all)


while True:
    print()
    month = int(input("Please select a month [1-12]: "))

    if month == 0:
        break

    while True:
        print()
        print("0. Back to the month selection")
        print("1. View all expenses")
        print("2. Add an expense")
        print("3. Statistics")

        choice = int(input("Choose an option: "))

        if choice == 0:
            break

        if choice == 1:
            show_expenses(month)

        if choice == 2:
            add_expense(month)

        if choice == 3:
            show_stats(month)
