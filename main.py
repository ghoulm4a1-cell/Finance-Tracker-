print("Welcome to the Personal Finance Tracker")



Income = 0
Expense = 0
Stop = True

while Stop:
    choice = input("What do you want to choose Income / Expenses / Savings / Quit? ").lower().strip()
    if choice == 'income':
        amount = int(input("Enter the amount: "))
        Income += amount
        print("Your income is updated!!")
        print(Income)
    elif choice == 'expense': 
        amount = int(input("Enter the amount: "))
        Expense += amount 
        print("Your expenses are updated!!")
        print(Expense)
    elif choice == 'savings': 
        Savings = int(Income) - int(Expense)
        print(f"Your Savings are: {Savings}")
    elif choice == 'quit': 
        Stop = False
        print("GoodBye!")
    else:
        print("Wrong Input !!")
        print("Please try again !!")
        
# Update 1. Made input user-friendly, 2. Removed unnecessary variables, 