for i in range (0,3):
    password = input("Enter the 4 digit pass code: ({} tries left) ".format(3 - i)) # password is 1234
    if password == '1234':
        print("Login was successful.")
        break
    elif i == 2:
        print("Your card has been blocked!")
    else:
        print("Incorrect password. Try again.")

balance = int(input("Enter your balance: "))

print("1) Check Balance")
print("2) Deposit")
print("3) Withdraw")
print("4) Cash Denomination Breakdown")
print("5) Change PIN")
print("6) Compound Interest Calculator (Demo)")
print("0) Exit")

choice = int(input("Your choice: "))

if choice == 1: # Check Balance
    print(f"Your balance is: {balance:,.0f}")
elif choice == 2: # Deposit
    while True:
        deposit = int(input("Enter the amount of deposit: "))
        if deposit <= 0:
            print("Error")
        else:
            new_balance = balance + deposit
            print(f"Your new balance (after the deposit) is {new_balance}")
            break
elif choice == 3: # Withdraw
    while True:
        withdraw = int(input("Enter the amount that you wanna withdraw: "))
        if withdraw <= 0:
            print("Amount must be positive!")
            continue
        elif withdraw % 50000 != 0:
            print("Error: Amount must be multiple of 50,000")
            continue
        elif withdraw > balance:
            print("Error: Not enough balance!")
            continue
        else:
            new_balance = balance - withdraw
            print(f"Your new balance (after the withdraw) is {new_balance:,.0f}")
            break
elif choice == 4: # Cash Denomination Breakdown
    while True:
        CDB=int(input("Whats the amount you wanna change? "))
        if CDB <= 0:
            print("Amount must be positive!")
            continue
        elif CDB % 50000 != 0:
            print("Error: Amount must be multiple of 50,000")
            continue
        elif CDB > balance:
            print("Error: Not enough balance!")
            continue
        else:
            five_hundred_thousands = CDB // 500000
            remainder = CDB % 500000

            two_hundred_thousands = remainder // 200000
            remainder = remainder % 200000

            one_hundred_thousands = remainder // 100000
            remainder = remainder % 100000

            fifty_thousands = remainder // 50000

            print(f"\nFor {CDB:,} Rials:")
            print(f"500,000 Rials: {five_hundred_thousands} bills")
            print(f"200,000 Rials: {two_hundred_thousands} bills")

            print(f"100,000 Rials: {one_hundred_thousands} bills")
            print(f"50,000 Rials: {fifty_thousands} bills")
            total_bills = (five_hundred_thousands + two_hundred_thousands +
                           one_hundred_thousands + fifty_thousands)
            print(f"Total bills used: {total_bills}")

            break
elif choice == 5: # Change PIN
    while True:
        old_pin = input("Enter your current PIN: ")
        if old_pin != '1234':
            print("Your current PIN that you entered is not correct")
        else:
            new_pin = input("Enter the new PIN: (4 digits) ")
            if not new_pin.isdigit():
                print("Invalid PIN: PIN must contain only numbers")
            elif len(new_pin) != 4:
                print("Invalid PIN: PIN must be exactly 4 digits")
            else:
                print("PIN changed successfully!")
                print(f"Your new PIN is: {new_pin}")
                break
elif choice == 6: #  Compound Interest Calculator

    principle = 0
    rate = 0
    time = 0

    while principle <= 0:
        principle = float(input("Enter the Principle amount: "))
        if principle <= 0:
            print("Principle cant be less than or equal to zero")

    while rate <= 0:
        rate = float(input("Enter the interest rate: "))
        if rate <= 0:
            print("Interest rate cant be less than or equal to zero")

    while time <= 0:
        time = int(input("Enter the time in years: "))
        if time <= 0:
            print("Time cant be less than or equal to zero")

    total = principle * pow((1 + rate / 100), time)
    print(f"Balance after {time} year/s : ${total:.2f}")
elif choice == 0: # exit
    print("Thank you for using our banking system. Goodbye!")
    exit()