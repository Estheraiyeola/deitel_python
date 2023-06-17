"""Target Heart-Rate Calculator"""
age = int(input("Enter your age: "))

maximum_heart_rate = 220 - age

heart_rate_1 = maximum_heart_rate / 100 * 50
heart_rate_2 = maximum_heart_rate / 100 * 85

print("Maximum heart rate is", maximum_heart_rate, "and the target heart rate zone is", heart_rate_1, "-", heart_rate_2)
