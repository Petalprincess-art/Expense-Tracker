class ExpenseTracker:
    def __init__(self):
        self.expenses = {}

    def add_expense(self):
        date = input("Enter the date (YYYY-MM-DD): ")
        category = input("Enter the category (e.g., food, transportation): ")
        amount = float(input("Enter the amount: "))
        description = input("Enter a description: ")

        if date not in self.expenses:
            self.expenses[date] = []

        self.expenses[date].append({
            "category": category,
            "amount": amount,
            "description": description
        })

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return

        for date, expenses_list in self.expenses.items():
            print(f"\nDate: {date}")
            for expense in expenses_list:
                print(f"  Category: {expense['category']}")
                print(f"  Amount: {expense['amount']}")
                print(f"  Description: {expense['description']}\n")

    def calculate_total(self):
        total_amount = sum(exp["amount"] for expenses_list in self.expenses.values() for exp in expenses_list)
        print(f"\nTotal expenses: {total_amount:.2f}\n")

def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            tracker.add_expense()
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            tracker.calculate_total()
        elif choice == "4":
            print("Exiting the tracker. Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
