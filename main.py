print("-------------------------------------------")
print("Welcome to the Personal Finance Tracker !!")
print("-------------------------------------------")


file_name = "Finance.txt"

def load_data():
    try:
        with open(file_name, 'r') as file:
            Income = float(file.readline())
            Expense = float(file.readline())
            return Income, Expense
    except FileNotFoundError:
        return 0, 0
    except ValueError:
        return 0, 0
    
def save_data(Income, Expense):
    with open(file_name, 'w') as file:
        file.write(str(Income)+ "\n")
        file.write(str(Expense)+ "\n")
               
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

Income, Expense = load_data()
Stop = True

while Stop:
    print("Choose an option:")
    print("Income / Expense / Savings / Quit")

    choice = input("Enter your choice: ").lower().strip() #used strips so that there shouldn't be any whitespaces remains

    if choice == "income":
        Income = add_income(Income)
    elif choice == "expense":
        Expense = add_expense(Expense)
    elif choice == "savings":
        show_summary(Income, Expense)
    elif choice == "quit":
        save_data(Income, Expense)
        print("Data Saved!! Goodbye!")
        Stop = False
    else:
        print("Invalid choice. Please try again.")

    
