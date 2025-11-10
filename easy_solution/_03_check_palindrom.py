import math

n = int(input("Enter the number to check palindrome:-> "))


def check_palindrome(num):
    original_num = num
    result = 0

    while num > 0:
        last_digit = num % 10
        result = (result * 10) + last_digit
        num = math.floor(num / 10)

    return original_num == result


# Check and print result
if check_palindrome(n):
    print(f"{n} is a palindrome.")
else:
    print(f"{n} is not a palindrome.")
