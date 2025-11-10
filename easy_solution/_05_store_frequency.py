# frequency map/dictionary
# store frequency in dictionary

nums = list(map(int, input("Enter the numbers separated by space:-> ").split()))


# def frequency(num):
#     freq_map = {}
#     for num in nums:
#         if num in freq_map:
#             freq_map[num] += 1
#         else:
#             freq_map[num] = 1
#     return freq_map
#
# print("The frequency of all the numbers is: {}".format(frequency(nums)))

# t.c = o(n)
# s.p = o(n)


# method-2 ->

def freq(n):
    freq_map = {}
    num = len(nums)
    for num in range(0,num):
        freq_map[nums[num]] = freq_map.get(nums[num], 0) + 1
    return freq_map
print(freq(nums))



