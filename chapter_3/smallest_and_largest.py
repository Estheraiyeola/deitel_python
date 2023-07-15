counter = 0
sum_ = 0
created_list = []
for input_ in range(0, 4):
    input_ = int(input('Enter the number: '))
    created_list.append(input_)
    sum_ += input_
    counter += 1
created_list.sort()
print('The largest number is', created_list[-1])
print('The smallest number is', created_list[0])
print('The sum of the numbers are', sum_)
print('The average of the numbers are', sum_ / counter)

