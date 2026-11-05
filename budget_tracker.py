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