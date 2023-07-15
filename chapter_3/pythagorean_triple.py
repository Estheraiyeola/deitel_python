for hypotenuse in range(1, 21):
    for side_1 in range(1, 21):
        for side_2 in range(1, 21):
            hypotenuse_square = hypotenuse ** 2
            sum_of_sides_squared = (side_1 ** 2) + (side_2 ** 2)

            if sum_of_sides_squared == hypotenuse_square:
                print(side_1, side_2, hypotenuse)
