account_balance = 20000
correct_pin = "1234"
attempts = 0
max_attempts = 3
print("----------------------")
print(             "WELCOME TO POS")
print("----------------------")
while attempts < max_attempts:
    entered_pin = input("Enter your  PIN: ")

    if entered_pin == correct_pin:
        print("PIN accepted.")
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        print("Incorrect PIN.")
        print("Attempts remaining:", remaining)

if attempts == max_attempts:
        print("Transaction declined. Too many PIN attempts.")

else:
    # Step 2: Ask for the transaction amount
    amount_text = input("Enter withdrawal amount in naira: ")

    if not amount_text.isdigit():
        print("Invalid amount. Enter numbers only.")

    else:
        amount = int(amount_text)

        # Step 3: Check the withdrawal amount
        if amount <= 0:
            print("Invalid amount. Amount must be greater than zero.")

        elif amount > account_balance:
            print("Insufficient balance.")

        else:
            # Step 4: Complete the transaction
            account_balance = account_balance - amount

            print("\nTRANSACTION SUCCESSFUL")
            print("Amount withdrawn: ₦", amount)
            print("Available balance: ₦", account_balance)

            print("\nPlease take your cash.")
            print("Thank you for using our POS.")
