import random


def generate_card_number():
    account_id = str(random.randint(0, 99999999))
    card_number = '400000' + '0' * (9 - int(len(account_id))) + account_id

    summa = 0
    for ind, n in enumerate(card_number):
        if ind % 2 == 0:
            n = int(n) * 2

        if int(n) > 9:
            n = int(n) - 9

        summa += int(n)

    checksum = str(10 - summa % 10)
    if checksum == '10':
        checksum = '0'
    print(summa)
    print(summa % 10)
    print(checksum)
    return card_number + checksum


def create_account():
    card_number = generate_card_number()
    card_pin = str(random.randint(0, 9999))
    card_pin = '0' * (4 - int(len(card_pin))) + card_pin

    bank_db[card_number] = {
        "pin": card_pin,
        "balance": 0.0
    }

    print("Your card has been created")
    print("Your card number:")
    print(card_number)
    print("Your pin:")
    print(card_pin)


def print_main_menu():
    while True:
        print("1. Create an account")
        print("2. Log in into account")
        print("0. Exit")

        choice = int(input())
        if choice == 1:
            create_account()
        if choice == 2:
            pass
        if choice == 0:
            print("Bye!")
            exit(0)


bank_db = {}
print_main_menu()