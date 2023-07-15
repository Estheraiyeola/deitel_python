"""Factorial calculator"""


def check_factorial(num):
    total = 1
    for num in range(num, 1, -1):
        total = num * total
    print(total)


check_factorial(5)
