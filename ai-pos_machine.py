
import json
import os

# POS settings
correct_pin = "1234"
max_attempts = 3
data_file = "pos_data.json"


# Step 1: Load saved account data
def load_data():
    if not os.path.exists(data_file):
       return {
       "balance": 20000,
       "history": [],
       "pin": "1234"
    }
    try:
        with open(data_file, "r") as file:
            data = json.load(file)

        if (
            not isinstance(data, dict)
            or not isinstance(data.get("balance"), int)
            or isinstance(data.get("balance"), bool)
            or data["balance"] < 0
            or not isinstance(data.get("history"), list)
            or not all(isinstance(item, str) for item in data["history"])
        ):
            raise ValueError("Invalid saved account data.")

        return data

    except (json.JSONDecodeError, ValueError) as error:
        print("Saved data is invalid:", error)
        print("Please check pos_data.json before continuing.")
        raise SystemExit(1)


# Step 2: Save account data
def save_data():
    data = {
        "balance": account_balance,
        "history": transaction_history,
        "pin": correct_pin

    }

    with open(data_file, "w") as file:
        json.dump(data, file, indent=4)

# Step 3: Verify PIN before an action
def verify_pin():
    attempts = 0

    while attempts < max_attempts:
        entered_pin = input("Enter your PIN to continue: ")

        if entered_pin == correct_pin:
            print("PIN verified.")
            return True

        attempts += 1
        print("Incorrect PIN.")
        print("Attempts remaining:", max_attempts - attempts)

    print("Access denied. Please try again later.")
    return False


def change_pin():
    global correct_pin

    while True:
        new_pin = input("Enter your new 4-digit PIN: ").strip()

        if len(new_pin) != 4 or not new_pin.isdigit():
            print("ERROR: PIN must contain exactly 4 digits.")
        elif new_pin == correct_pin:
            print("ERROR: Choose a different PIN.")
        else:
            confirm_pin = input("Confirm your new PIN: ").strip()

            if confirm_pin != new_pin:
                print("ERROR: PINs do not match.")
            else:
                correct_pin = new_pin
                save_data()
                print("PIN changed successfully.")
                break

# Load saved data when the program starts
saved_data = load_data()
account_balance = saved_data["balance"]
transaction_history = saved_data["history"]
correct_pin = saved_data.get("pin", "1234")


print("----------------------")
print("WELCOME TO POS")
print("----------------------")


# Step 4: Display the POS menu
while True:
    print("\n========== POS MENU ==========")
    print("1. Withdraw money")
    print("2. Check account balance")
    print("3. Transfer money")
    print("4. View transaction history")
    print("5. Change pin")
    print("6. Exit")
    print("==============================")

    choice = input("Choose an option (1-6): ")

    if choice == "6":
        print("Thank you for using our POS.")
        break

    elif choice in ["1", "2", "3", "4", "5"]:

        # Verify PIN before continuing
        if not verify_pin():
            continue

        # Option 1: Withdraw money
        if choice == "1":
            amount_text = input("Enter withdrawal amount: ")

            if not amount_text.isdigit():
                print("Invalid amount.")

            else:
                amount = int(amount_text)

                if amount <= 0:
                    print("Amount must be greater than zero.")

                elif amount > account_balance:
                    print("Insufficient balance.")

                else:
                    account_balance -= amount
                    transaction_history.append(
                        f"Withdrawal: ₦{amount}"
                    )
                    save_data()

                    print("Withdrawal successful.")
                    print("Available balance: ₦", account_balance)

        # Option 2: Check balance
        elif choice == "2":
            print("Your balance is: ₦", account_balance)

        # Option 3: Transfer money
        
        # Option 3: Transfer money
        elif choice == "3":
            while True:
                recipient = input(
                    "Enter recipient account number: "
                ).strip()

                if len(recipient) != 10 or not recipient.isdigit():
                    print("ERROR: Enter a valid 10-digit account number.")
                else:
                    break

            amount_text = input("Enter transfer amount: ")

            if not amount_text.isdigit():
                print("Invalid amount.")

            else:
                amount = int(amount_text)

                if amount <= 0:
                    print("Amount must be greater than zero.")

                elif amount > account_balance:
                    print("Insufficient balance.")

                else:
                    account_balance -= amount
                    transaction_history.append(
                        f"Transfer to {recipient}: ₦{amount}"
                    )
                    save_data()

                    print("Transfer recorded successfully.")
                    print("Available balance: ₦", account_balance)

        # Option 4: View transaction history
        elif choice == "4":
            if not transaction_history:
                print("No transactions yet.")

            else:
                print("\nTRANSACTION HISTORY")

                for transaction in transaction_history:
                    print(transaction)
        elif choice == "5":
           change_pin()

    else:
        print("Invalid option. Choose between 1 and 5.")
