import math

n = int(input("enter a number:->"))

nums=n

while nums > 0:
    last_digit = nums % 10
    print(last_digit)
    nums = math.floor(nums//10)


