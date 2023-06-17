"""Arithmetic, Smallest and Largest"""

input_1 = int(input('Enter the first integer: '))
input_2 = int(input('Enter the second integer: '))
input_3 = int(input('Enter the third integer: '))

sum_of_numbers = input_1 + input_2 + input_3
average = sum_of_numbers / 3
product = input_1 * input_2 * input_3

smallest = input_1
if input_2 < smallest:
	smallest = input_2
if input_3 < smallest:
	smallest = input_3
	
largest = input_1
if input_2 > largest:
	largest = input_2
if input_3 > largest:
	largest = input_3


print('Sum of the three numbers is', sum_of_numbers)
print('Average of the three numbers is', average)
print('Product of the three numbers is', product)
print('The smallest number is', smallest)
print('The largest number is', largest)
