

def check_palindrome(n):
    reversed_num = 0
    original_number = n

    while n != 0:
        current_num = n % 10
        reversed_num = reversed_num * 10
        reversed_num = reversed_num + current_num
        n = n // 10
    if original_number == reversed_num:
        print(original_number, 'is palindrome')
    else:
        print(original_number, 'is not palindrome')
    return n


check_palindrome(212)