
def get_valid_amount():
    
    while True:
        user_input = input("Enter expense amount (Rs.): ").strip()
        try:
            amount = float(user_input)
        except ValueError:
            print("Invalid input. Please enter a number (e.g. 250 or 99.50).")
            continue

        if amount < 0:
            print("Expense amount cannot be negative. Please try again.")
            continue

        return amount


def add_expense(expenses):
    
    amount = get_valid_amount()
    expenses.append(amount)
    print(f"Expense of Rs. {amount:.2f} added. "
          f"Total expenses recorded so far: {len(expenses)}")


def calculate_total(expenses):
    
    total = 0.0
    for amount in expenses:
        total = total + amount  
    return total


def view_summary(expenses):
    
    print("\n----- Expense Summary -----")

    if len(expenses) == 0:
        print("No expenses have been added yet.")
    else:
        total = calculate_total(expenses)
        average = total / len(expenses)

        print(f"Number of expenses : {len(expenses)}")
        print(f"Total spent        : Rs. {total:.2f}")
        print(f"Average expense    : Rs. {average:.2f}")

    


def show_menu():
    
    print(" Expense Tracker Menu")
    print("1. Add Expense")
    print("2. View Total Spent")
    print("3. Exit")
    


def main():
    
    expenses = []  
    running = True

    print("Welcome to the DecodeLabs Expense Tracker.\n")

    while running:
        show_menu()
        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_summary(expenses)
        elif choice == "3":
            print("\nThank you for using the Expense Tracker. Goodbye!")
            running = False
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

        print()  


if __name__ == "__main__":
    main()