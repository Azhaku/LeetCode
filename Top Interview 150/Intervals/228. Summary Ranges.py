# You are given a sorted unique integer array nums.

# A range [a,b] is the set of all integers from a to b (inclusive).

# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

# Each range [a,b] in the list should be output as:

# "a->b" if a != b
# "a" if a == b
 

# Example 1:

# Input: nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: The ranges are:
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"
# Example 2:

# Input: nums = [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: The ranges are:
# [0,0] --> "0"
# [2,4] --> "2->4"
# [6,6] --> "6"
# [8,9] --> "8->9"
 

# Constraints:

# 0 <= nums.length <= 20
# -231 <= nums[i] <= 231 - 1
# All the values of nums are unique.
# nums is sorted in ascending order.




# method 1: time O(n), space worst case O(n)[res can't be in constant space]
class Solution(object):
    def summaryRanges(self, nums):
        start = 0
        end = 0
        s = ''
        i = 0
        res = []
        if len(nums) == 0:
            return res
        if len(nums) ==1:
            res.append(str(nums[0]))
            return res

        while i<len(nums)-1:
            if nums[i]+1 != nums[i+1]:
                if start == i:
                    res.append(str(nums[i]))
                elif start != i:
                    s = str(nums[start]) + "->" + str(nums[i])
                    res.append(s)
                start = i+1 
            i+=1

        if start == i:
            res.append(str(nums[i]))
        elif start != i:
            s = str(nums[start]) + "->" + str(nums[i])
            res.append(s)

        return res
    
#method 2: time O(n), little optimized than the above one
class Solution(object):
    def summaryRanges(self, nums):
        end = 0
        start = 0
        res = []
        if len(nums) == 0:
            return res
        if len(nums) ==1:
            res.append(str(nums[0]))
            return res

        while start<len(nums):
            end = start
            while end+1 < len(nums) and nums[end+1] == nums[end]+1:
                end +=1
            if end != start:
                res.append(str(nums[start]) + "->" + str(nums[end]))
            else:
                res.append(str(nums[start]))
            start = end+1
        return res

n = []   
s = Solution()
print(s.summaryRanges(n))