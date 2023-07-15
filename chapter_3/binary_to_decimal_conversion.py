"""Binary numbers converter"""
number = "1111"


def converter(binary_number):
    decimal_number = 0
    multiplier = 1
    numbers = int(binary_number) / 10
    remainder = int(binary_number) % 10
    decimal_number += remainder * multiplier
    binary_number = int(numbers)
    while int(binary_number) >= 1:
        numbers = int(binary_number) / 10
        remainder = int(binary_number) % 10
        multiplier *= 2
        decimal_number += remainder * multiplier
        binary_number = int(numbers)
        if int(numbers) < 1:
            break
    return decimal_number


print(converter(number))
