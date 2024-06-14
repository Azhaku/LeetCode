# Given an array of positive integers nums and a positive integer target, return the minimal length of a 
# subarray
#  whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1
# Example 3:

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
 
 
# print(min(0,float("inf")))

class Solution(object):
    def minSubArrayLen(self, target, nums):
        start = 0
        small = len(nums)+1
        total = 0
        for end in range(0,len(nums)):
            total += nums[end]
            while total >= target:
                small = min(small,( end - start)+1)
                total -= nums[start]
                start +=1
        if small < len(nums)+1:
            return small
        else:
            return 0
                
s = Solution()
min_elements = s.minSubArrayLen(7,[2,3,1,2,4,3])
assert 2 == min_elements