import csv

FILE_NAME = "budget_data.csv"

def initialize_budget_file():
    """Initialize the budget data file if it doesn't exist."""
    try:
        with open(FILE_NAME, mode='x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Type", "Amount", "Description"])
    except FileExistsError:
        pass  # File already exists, no need to initialize

def add_income(amount, description):
    """Add income to the budget data file."""
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([get_current_date(), "Income", amount, description])

def add_expense():
    """Add expense to the budget data file."""
    category = input("Enter the category of the expense: ")
    amount = float(input("Enter the amount of the expense: "))
    description =  input("Enter a description for the expense: ")
    date = input("Enter the date of the expense (YYYY-MM-DD): ")
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

    print(f"Expense of £{amount} in category '{category}' has been added to your budget.")

def view_expenses():
    """Display all expenses from the budget data file."""
    with open(FILE_NAME, mode='r') as file:
        reader = csv.DictReader(file)
        print("\nExpenses:")
        for row in reader:
            if row["Type"] == "Expense":
                print(f"Date: {row['Date']}, Category: {row['Category']}, Amount: £{row['Amount']}, Description: {row['Description']}")    

def view_current_balance():
    """Calculate and display the current balance."""
    balance = {}
    total_balance = 0.0

    with open(FILE_NAME, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])
            if category not in balance:
                balance[category] = 0.0
            balance[category] += amount
            total_balance += amount

    print("\nCurrent Balance by Category:")
    for category, amount in balance.items():
        print(f"{category}: £{amount:.2f}")
    print(f"\nTotal Balance: £{total_balance:.2f}")

print("Welcome to the Budget Tracker!")

print("\nThis program will help you track your expenses and manage your budget effectively.\n")

income = 0.0
expense = 0.0

while True:
    print("Please choose an option from the menu below to get started:\n")
    print("1. Add Income")
    print("2. Add Expenses")
    print("3. View current balance")
    print("4. Exit")

    option = input("\nEnter your choice (1-4): ")

    print("You selected option:", option)

    if option == "1":
        amount = float(input("Enter the amount of income: "))
        income += amount
        print(f"Income of £{amount:.2f} has been added to your budget.")
    elif option == "2":
        amount = float(input("Enter the amount of expense: "))
        expense += amount
        print(f"Expense of £{amount} has been added to your budget.")
    elif option == "3":
        current_balance = income - expense
        print(f"Your current balance is: £{current_balance}")
    elif option == "4":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")

