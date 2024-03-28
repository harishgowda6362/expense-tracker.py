class ExpenseTracker:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, amount, category):
        self.transactions.append({'amount': amount, 'category': category})
        print(f"Transaction added: ${amount} in '{category}' category.")

    def view_transactions(self):
        if self.transactions:
            print("Your Transactions:")
            for idx, transaction in enumerate(self.transactions, start=1):
                print(f"{idx}. ${transaction['amount']} in '{transaction['category']}'")
        else:
            print("No transactions recorded yet.")

    def calculate_total_expenses(self):
        total_expenses = sum(transaction['amount'] for transaction in self.transactions)
        print(f"Total expenses: ${total_expenses}")

def main():
    tracker = ExpenseTracker()
    while True:
        print("\n1. Add Transaction\n2. View Transactions\n3. Calculate Total Expenses\n4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            amount = float(input("Enter transaction amount: "))
            category = input("Enter transaction category: ")
            tracker.add_transaction(amount, category)
        elif choice == "2":
            tracker.view_transactions()
        elif choice == "3":
            tracker.calculate_total_expenses()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()