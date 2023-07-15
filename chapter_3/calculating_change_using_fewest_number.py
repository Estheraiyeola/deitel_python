"""Change calculator"""
amount_payed = 1
price_of_purchased_item = 1.75
balance1 = amount_payed - price_of_purchased_item


def calculator(balance):
    dime = 0
    pennies = 0
    quarter = 0
    divisor = balance % 1
    new_number = divisor * 100
    if balance % 2 == 0:
        return print(f'''
        You have ${int(balance)} change please''')
    if balance < 0:
        return print(f'''
            You still owe ${balance}''')
    if new_number >= 25:
        quarter = new_number / 25
        new_number = new_number % 25
    if new_number >= 10:
        dime = new_number / 10
        pennies = new_number % 10
    return print(f'''
    Your change is:
    {int(quarter)} quarters
    {int(dime)} dimes
    {int(pennies)} pennies''')


print(calculator(balance1))
