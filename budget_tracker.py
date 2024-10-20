import csv
import os

# File to store budget data
BUDGET_FILE = 'budget.csv'


# Check if the budget file exists, otherwise create it
def initialize_file():
    if not os.path.exists(BUDGET_FILE):
        with open(BUDGET_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Type', 'Amount', 'Category', 'Description'])


# Add a new transaction
def add_transaction(transaction_type, amount, category, description):
    with open(BUDGET_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([transaction_type, amount, category, description])
    print(f'Added {transaction_type}: ${amount} for {category} - {description}')


# Calculate the current balance
def calculate_balance():
    balance = 0
    with open(BUDGET_FILE, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            amount = float(row['Amount'])
            if row['Type'].lower() == 'income':
                balance += amount
            elif row['Type'].lower() == 'expense':
                balance -= amount
    return balance


# List all transactions or filter by category
def list_transactions(filter_category=None):
    with open(BUDGET_FILE, 'r') as file:
        reader = csv.DictReader(file)
        print(f"{'Type':<10} {'Amount':<10} {'Category':<15} {'Description':<30}")
        print("=" * 65)
        for row in reader:
            if filter_category is None or row['Category'].lower() == filter_category.lower():
                print(f"{row['Type']:<10} {row['Amount']:<10} {row['Category']:<15} {row['Description']:<30}")


# Remove a transaction by description
def remove_transaction(description):
    transactions = []
    found = False
    with open(BUDGET_FILE, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Description'] == description:
                found = True
                continue
            transactions.append(row)

    if found:
        with open(BUDGET_FILE, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Type', 'Amount', 'Category', 'Description'])
            writer.writeheader()
            writer.writerows(transactions)
        print(f'Removed transaction: {description}')
    else:
        print('Transaction not found.')


# Main menu
def main():
    initialize_file()

    while True:
        print("\nPersonal Budget Tracker")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Balance")
        print("4. List Transactions")
        print("5. List Transactions by Category")
        print("6. Remove Transaction")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            amount = float(input("Enter income amount: "))
            category = input("Enter income category: ")
            description = input("Enter description: ")
            add_transaction('Income', amount, category, description)
        elif choice == '2':
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")
            description = input("Enter description: ")
            add_transaction('Expense', amount, category, description)
        elif choice == '3':
            balance = calculate_balance()
            print(f'Current Balance: ${balance:.2f}')
        elif choice == '4':
            list_transactions()
        elif choice == '5':
            category = input("Enter category to filter by: ")
            list_transactions(filter_category=category)
        elif choice == '6':
            description = input("Enter the description of the transaction to remove: ")
            remove_transaction(description)
        elif choice == '7':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == '__main__':
    main()
