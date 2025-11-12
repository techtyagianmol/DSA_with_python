class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # nums.sort()  # sort first
        # left = 0
        # right = 1

        # while right < len(nums):
        #     if nums[left] == nums[right]:
        #         return True  # found duplicate
        #     left += 1
        #     right += 1

        # return False
        # t.c -> O(n log n) due to sorting
        # s.c -> O(1)


        # 2 approach using set 
        
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
            
        # # t.c -> O(n)
        # # s.c -> O(n)