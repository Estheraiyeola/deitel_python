"""Separating the numbers in an integer"""
number = int(input("Enter the integer: "))

first_number_1 = int(number / 10000)

second_number = int(number / 1000)
second_number_2 = second_number % 10

third_number = int(number / 100)
third_number_3 = third_number % 10

fourth_number = int(number / 10)
fourth_number_4 = fourth_number % 10

fifth_number_5 = number % 10

print(first_number_1, "\t", second_number_2, "\t", third_number_3, "\t", fourth_number_4, "\t", fifth_number_5)
