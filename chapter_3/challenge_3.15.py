"""Challenge: Approximating the Mathematical Constant e"""


def check_factorial(n):
    total = 1
    for n in range(n, 1, -1):
        total = n * total
    return total


num = int(input('Enter the number: '))
sum_ = 1
k = 1
for e in range(1, num + 1):
    sum_ = sum_ + 1 / check_factorial(k)
    k += 1
print(sum_)
