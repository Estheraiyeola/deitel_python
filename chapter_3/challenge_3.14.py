"""Challenge: Approximating the Mathematical Constant"""
k = 1
sum_ = 0
print(f'number of series\t\tvalue of pi', end='\n')
for pi in range(0, 100000):
    if pi % 2 == 0:
        sum_ += 4 / k
    else:
        sum_ -= 4 / k
    print(f'{pi}\t\t\t\t\t\t{sum_}')
    k = k + 2
