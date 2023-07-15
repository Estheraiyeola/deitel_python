

def get_asterisks(number):
    row = number
    while row >= 1:
        space = number
        while space > row:
            print(' ', end=' ')
            space -= 1
        column = 1
        while column <= row:
            print('*', end=' ')
            column += 1
        print()
        row -= 1


get_asterisks(4)