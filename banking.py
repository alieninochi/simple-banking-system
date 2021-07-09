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