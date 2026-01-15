print("Welcome to the Personal Finance Tracker !!")

Income = 0
Expense = 0
Stop = True

def add_income(Income):
    while True:
        amount = input("Enter the amount: ")
        try: 
            amount = float(amount)
            Income += amount
            print("Income updated Successfully!")
            print("Total Income: ", Income)
            break
        except:
            print("Please enter a valid number.")
    return Income

def add_expense(Expense):
    while True:
        amount = input("Enter the amount: ")
        try: 
            amount = float(amount)
            Expense += amount
            print("Expense Updated Successfully!")
            print("Total Expense: ", Expense)
            break
        except:
            print("Please enter a valid number.")
    return Expense

def show_summary(Income, Expense):
            Savings = Income - Expense
            print("\n ---Summary---")
            print("Income:",Income)
            print("Expense:",Expense)
            print("Savings:", Savings)



while Stop:
    print("\nChoose an option:")
    print("Income / Expense / Savings / Quit")

    choice = input("Enter your choice: ").lower().strip() #used strips so that there shouldn't be any whitespaces remains

    if choice == "income":
        Income = add_income(Income)
    elif choice == "expense":
        Expense = add_expense(Expense)
    elif choice == "savings":
        Savings = show_summary(Income, Expense)
    elif choice == "quit":
        print("Thanks for using the Finance Tracker. Goodbye!")
    else:
        print("Invalid choice. Please try again.")

    
