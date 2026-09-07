# Simple Banking Application

balance = 0
account_created = False
name = ""
account_number = ""

while True:
    print("\n===== BANKING APPLICATION =====")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    # Create Account
    if choice == 1:
        name = input("Enter your name: ")
        account_number = input("Enter account number: ")

        account_created = True

        print("Account created successfully!")

    # Deposit Money
    elif choice == 2:
        if not account_created:
            print("Please create an account first.")
        else:
            amount = float(input("Enter amount to deposit: "))

            if amount > 0:
                balance += amount
                print("Money deposited successfully.")
                print("Current Balance: Rs.", balance)
            else:
                print("Invalid amount.")

    # Withdraw Money
    elif choice == 3:
        if not account_created:
            print("Please create an account first.")
        else:
            amount = float(input("Enter amount to withdraw: "))

            if amount <= 0:
                print("Invalid amount.")
            elif amount > balance:
                print("Insufficient balance.")
            else:
                balance -= amount
                print("Money withdrawn successfully.")
                print("Current Balance: Rs.", balance)

    # Check Balance
    elif choice == 4:
        if not account_created:
            print("Please create an account first.")
        else:
            print("\nAccount Holder:", name)
            print("Account Number:", account_number)
            print("Current Balance: Rs.", balance)

    # Exit
    elif choice == 5:
        print("Thank you for using the Banking Application!")
        break

    # Invalid Choice
    else:
        print("Invalid choice. Please try again.")