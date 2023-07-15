"""Challenge: Nested Looping"""


def asterisks(num):
    for row in range(num):
        for column in range(row + 1):
            print('*', end=" ")
        for column in range(num - row, 0, -1):
            print(' ', end=" ")
        for column in range(num - row):
            print('*', end=" ")
        for column in range(row + 1):
            print(' ', end=" ")
        for column in range(row + 1):
            print(' ', end=" ")
        for column in range(num - row, 0, -1):
            print('*', end=" ")
        for column in range(num - row):
            print(' ', end=" ")
        for column in range(row + 1):
            print('*', end=" ")
        print()


asterisks(10)
