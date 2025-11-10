# print all foctors of the given number
import math

n = int(input("enter a number:->"))

def factorial(num):
#     result = []
#     for i in range (1,math.floor(n//2)+1):
#         if num % i == 0:
#             result.append(i)
#     result.append(num)
#
#     return result
# print("Factors are:", factorial(n))

    result = []
    for i in range(1,int(math.sqrt(num))+1):
        if num % i == 0:
            result.append(i)
            if num//i != i:
                result.append(num//i)
    result.sort()
    return result

print("factorial({}) = {}".format(n,factorial(n)))

# t.c = o(sqrt(n)+o(nlogn))
# sp.c = o(k)