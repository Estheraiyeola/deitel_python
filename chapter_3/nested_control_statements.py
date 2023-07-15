numbers = []
for user_input in range(10):
    numbers.append(int(input('Enter the number: ')))
numbers.sort()
print(numbers[-1])
print(numbers[-2])
