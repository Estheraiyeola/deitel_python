passes = 0


for student in range(10):
    result = int(input('Enter result (1=pass, 2=fail): '))
    if result == 1:
        passes += 1
    elif result == 2:
        passes += 0
    else:
        passes = 0
        result = int(input('Enter result (1=pass, 2=fail): '))
no_of_failure = 10 - passes
print(no_of_failure)


# result = int(input('Enter result (1=pass, 2=fail): '))
# while result == 1 or result == 2:
#     passes += 1
#     result = int(input('Enter result (1=pass, 2=fail): '))
# no_of_failure = 10 - passes
# print(no_of_failure, 'number of failures')