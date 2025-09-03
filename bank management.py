import os
import csv

# File to store account data
FILENAME = "bank_accounts.csv"

# Check if file exists, if not create it
if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["AccountNo", "Name", "AccountType", "Balance"])

# Function to load all accounts from file
def load_accounts():
    accounts = {}
    with open(FILENAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            accounts[row["AccountNo"]] = {
                "name": row["Name"],
                "type": row["AccountType"],
                "balance": float(row["Balance"])
            }
    return accounts

# Function to save accounts to file
def save_accounts(accounts):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["AccountNo", "Name", "AccountType", "Balance"])
        for acc_no, data in accounts.items():
            writer.writerow([acc_no, data["name"], data["type"], data["balance"]])

# Create new account
def create_account(accounts):
    name = input("Enter account holder name: ")
    acc_no = input("Enter account number: ")
    if acc_no in accounts:
        print("Account number already exists!\n")
        return
    acc_type = input("Enter account type (Savings/Current): ").capitalize()
    balance = float(input("Enter initial deposit: "))
    accounts[acc_no] = {"name": name, "type": acc_type, "balance": balance}
    save_accounts(accounts)
    print(f"Account created successfully for {name}.\n")

# Deposit money
def deposit(accounts):
    acc_no = input("Enter account number: ")
    if acc_no in accounts:
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Deposit amount must be positive.\n")
            return
        accounts[acc_no]["balance"] += amount
        save_accounts(accounts)
        print(f"Deposited successfully. New balance: {accounts[acc_no]['balance']}\n")
    else:
        print("Account not found!\n")

# Withdraw money
def withdraw(accounts):
    acc_no = input("Enter account number: ")
    if acc_no in accounts:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Withdrawal amount must be positive.\n")
            return
        if accounts[acc_no]["balance"] >= amount:
            accounts[acc_no]["balance"] -= amount
            save_accounts(accounts)
            print(f"Withdrawal successful. New balance: {accounts[acc_no]['balance']}\n")
        else:
            print("Insufficient balance!\n")
    else:
        print("Account not found!\n")

# Check balance
def check_balance(accounts):
    acc_no = input("Enter account number: ")
    if acc_no in accounts:
        data = accounts[acc_no]
        print(f"Account holder: {data['name']}")
        print(f"Account type: {data['type']}")
        print(f"Balance: {data['balance']}\n")
    else:
        print("Account not found!\n")

# Display all accounts
def display_accounts(accounts):
    if accounts:
        print("All Accounts:")
        for acc_no, data in accounts.items():
            print(f"Acc No: {acc_no}, Name: {data['name']}, Type: {data['type']}, Balance: {data['balance']}")
        print()
    else:
        print("No accounts found!\n")

# Main program
def main():
    while True:
        accounts = load_accounts()
        print("===== Advanced Bank Management System =====")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Display All Accounts")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            create_account(accounts)
        elif choice == "2":
            deposit(accounts)
        elif choice == "3":
            withdraw(accounts)
        elif choice == "4":
            check_balance(accounts)
        elif choice == "5":
            display_accounts(accounts)
        elif choice == "6":
            print("Thank you for using the Advanced Bank Management System!")
            break
        else:
            print("Invalid choice! Please try again.\n")

if __name__== "__main__":
    main()
