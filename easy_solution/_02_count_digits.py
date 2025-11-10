import math

n=int(input("enter a number:->"))

nums = n
cnt = 0

while nums > 0:
    cnt +=1
    nums=math.floor(nums//10)

print(cnt)


# time complaxity=?
# space complexity=?