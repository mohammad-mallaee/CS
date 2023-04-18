def check_number(num_str):
    i = num_str.find(".")
    if len(num_str) == 1:
        return num_str.isdigit()
    return num_str[:i].isdigit() and num_str[i + 1:].isdigit()


def parse_account_balance(balance_str):
    parsed_balance = balance_str
    convert_values = {
        "zero": "0", "one": "1", "two": "2",
        "three": "3", "four": "4",
        "five": "5", "six": "6",
        "seven": "7", "eight": "8",
        "nine": "9", "dot": "."
    }
    parsed_balance = parsed_balance.replace(",", "")
    for convert_sign in convert_values:
        convert_value = convert_values[convert_sign]
        parsed_balance = parsed_balance.replace(convert_sign, convert_value)
    return float(parsed_balance)


def parse_account_numbers(accounts_str):
    parsed_account_str = ""
    for char in accounts_str:
        if char.isdigit():
            parsed_account_str += char
    account_numbers = [int(parsed_account_str[i:i + 5]) for i in range(0, len(parsed_account_str), 5)]
    return account_numbers


def parse_accounts(accounts_str, balances_str):
    balances = list(map(parse_account_balance, balances_str.split("-")))
    account_numbers = parse_account_numbers(accounts_str)
    accounts = {}
    for i in range(len(balances)):
        accounts[account_numbers[i]] = balances[i]
    return accounts


def get_menu_option(account_number):
    print("\nYou're in, " + str(account_number) +
          "! What would you like to do?"
          "\n1) View Your Balance"
          "\n2) Deposit Money"
          "\n3) Withdraw Money"
          "\n4) Transfer Money"
          "\n5) Close Your Account"
          "\n6) Exit Your Account")
    while True:
        option_str = input("Enter the relevant number: ")
        if not option_str.isdigit() or not 1 <= int(option_str) <= 6:
            print("Incorrect input. You should choose a number between 1 and 6.")
            continue
        return int(option_str)


def get_account_number(accounts):
    while True:
        data = input("Please present your vault key (-1 for exiting): ")
        if data == "-1":
            return -1
        if not check_number(data) or int(data) not in accounts:
            print("The account number that you provided is wrong! Try again.\n")
            continue
        return int(data)


def view_balance(account_number, accounts):
    print("\nYour balance is:", accounts[account_number])


def deposit_money(account_number, accounts):
    while True:
        print("\n--- Depositing money")
        money = input("How much money you want to deposit (-1 for exiting)? ")
        if money == "-1":
            return
        if not check_number(money):
            print("Incorrect input! Try again.")
            continue
        money = float(money)
        accounts[account_number] += money
        print("Your balance is now:", accounts[account_number])
        if not confirm():
            return


def withdraw_money(account_number, accounts):
    while True:
        print("\n--- Withdrawing money")
        money = input("How much money you want to withdraw (-1 for exiting)? ")
        if money == "-1":
            return
        if not check_number(money):
            print("Incorrect input! Try again.")
            continue
        money = float(money)
        if money > accounts[account_number]:
            print("Your balance is not enough!")
            if not confirm():
                return
            continue

        accounts[account_number] -= money
        print("Your balance is now:", accounts[account_number])

        if not confirm():
            return


def transfer_money(account_number, accounts):
    while True:
        print("\n--- Transferring money")
        number = input("Account Number (-1 for exiting): ")
        if number == "-1":
            return
        money = input("Amount of money: ")
        if not check_number(money) or not check_number(number):
            print("Incorrect inputs. Try again")
            continue
        money = float(money)
        number = int(number)
        if number not in accounts:
            print("This account doesnt exist!")
            continue
        if money > accounts[account_number]:
            print("Your balance is not enough")
            continue
        accounts[account_number] -= money
        accounts[number] += money
        print("Money transferred successfully.")
        print("Your balance is now :", accounts[account_number])
        if not confirm():
            return


def close_account(account_number, accounts):
    print("\nYou can't access your account or money after closing your account.")
    if confirm("Do you want to close your account (yes/no)? "):
        del accounts[account_number]
        print("Account number", account_number, "is now closed and inaccessible.")


def confirm(confirmation_str="\nDo you want to continue (yes/no) ? "):
    while True:
        confirmation = input(confirmation_str)
        if confirmation.lower() == "no":
            return False
        if confirmation.lower() == "yes":
            return True
        print("Incorrect input. Try again")


functions = [view_balance, deposit_money, withdraw_money, transfer_money, close_account]


def start():
    print("--------------------------------------")
    print("|      Gringotts Wizarding Bank      |")
    print("--------------------------------------")
    print("\nEnter scrambled accounts string:")
    accounts_str = input()
    print("Enter balances string:")
    balances_str = input()
    accounts = parse_accounts(accounts_str, balances_str)
    services_count = 0
    while services_count < 10:
        services_count += 1
        print("\nWelcome to the Gringotts Wizarding Bank!")
        account_number = get_account_number(accounts)
        if account_number == -1:
            continue
        while True:
            menu_option = get_menu_option(account_number)
            if menu_option == 6:
                break
            functions[menu_option - 1](account_number, accounts)
            if menu_option == 5 and account_number not in accounts:
                break

    print("\nSorry, Gringotts is closed for the day. See you tomorrow!")


start()
