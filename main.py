print("Welcome to the Personal Finance Tracker !!")

Income = 0
Expense = 0
Stop = True

while Stop:
    print("\nChoose an option:")
    print("Income / Expense / Savings / Quit")

    choice = input("Enter your choice: ").lower().strip() #used strips so that there shouldn't be any whitespaces remains

    if choice == "income":
        while True:
            amount = input("Enter the amount: ")
            try: 
                amount = float(amount)
                Income += amount
                print("Income updated Successfully!")
                print("Total Income: ",Income)
                break
            except:
                print("Please enter a valid number.")
    elif choice == "expense":
        while True:
            amount = input("Enter the amount: ")
            try:
                amount = float(amount)
                Expense += amount
                print("Expense updated Successfully!")
                print("Total Expense: ", Expense)
                break
            except:
                print("Please enter a valid number.")
    elif choice == "savings":
        Savings = Income - Expense
        print("\n ---Summary---")
        print("Income:",Income)
        print("Expense:",Expense)
        print("Savings:", Savings)

    elif choice == "quit":
        print("Thanks for using the Finance Tracker. Goodbye!")
    else:
        print("Invalid choice. Please try again.")
