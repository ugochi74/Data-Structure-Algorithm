account_balance = 20000
correct_pin = "1234"
attempts = 0
max_attempts = 3
transaction_history = []
print("----------------------")
print(             "WELCOME TO POS")
print("----------------------")
pin_accepted = False

while attempts < max_attempts:
    entered_pin = input("Enter your PIN: ")

    if entered_pin == correct_pin:
        print("PIN accepted.")
        pin_accepted = True
        break
    else:
        attempts += 1
        print("Incorrect PIN.")
        print("Attempts remaining:", max_attempts - attempts)

# Step 2: Show the menu only if the PIN is correct
if not pin_accepted:
    print("Transaction declined. Too many PIN attempts.")

else:
    while True:
        print("\n========== POS MENU ==========")
        print("1. Withdraw money")
        print("2. Check account balance")
        print("3. Transfer money")
        print("4. View transaction history")
        print("5. Exit")
        print("==============================")

        choice = input("Choose an option (1-5): ")

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

                    print("Transaction successful.")
                    print("Amount withdrawn: ₦", amount)
                    print("Available balance: ₦", account_balance)

        # Option 2: Check balance
        elif choice == "2":
            print("Your balance is: ₦", account_balance)

        # Option 3: Transfer money
        elif choice == "3":
            recipient = input("Enter recipient account number: ")
            amount_text = input("Enter transfer amount: ")

            if not recipient.strip():
                print("Account number cannot be empty.")

            elif not amount_text.isdigit():
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

                    print("Transfer successful.")
                    print("Recipient:", recipient)
                    print("Amount transferred: ₦", amount)
                    print("Available balance: ₦", account_balance)

        # Option 4: View transaction history
        elif choice == "4":
            if not transaction_history:
                print("No transactions yet.")

            else:
                print("\nTRANSACTION HISTORY")

                for transaction in transaction_history:
                    print(transaction)

        # Option 5: Exit
        elif choice == "5":
            print("Thank you for using our POS.")
            break

        else:
            print("Invalid option. Choose between 1 and 5.")
