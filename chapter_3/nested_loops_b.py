def get_asterisks(number):
    for row in range(number, 0, -1):
        for column in range(0, row):
            print("*", end='')
        print()


get_asterisks(10)
