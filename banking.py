import random


def create_account():
    account_id = str(random.randint(0, 9999999999))
    card_number = '400000' + '0' * (10 - int(len(account_id))) + account_id
    card_pin = str(random.randint(0, 9999))
    card_pin = '0' * (4 - int(len(card_pin))) + card_pin

    print("Your card has been created")
    print("Your card number:")
    print(card_number)
    print("Your pin:")
    print(card_pin)


def print_menu():
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