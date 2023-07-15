
def get_asterisks(number):
    for row in range(number):
        for column in range(row):
            print("*", end='')
        print()

get_asterisks(10)