
def get_asterisks(number):
    space = 2 * number - 2
    for row in range(0, number):
        for column in range(0, space):
            print(" ", end="")
        space = space - 2
        for column in range(0, row + 1):
            print("*", end=" ")
        print("")


get_asterisks(10)
