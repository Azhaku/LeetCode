# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
 

# Constraints:

# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105

# method-1: O(n^2)
class Solution(object):
    def threeSum(self, nums):
        res = []
        nums = sorted(nums)
        for i, val in enumerate(nums[:-2]):
            left, right =i+1 , len(nums)-1
            if i>0 and val == nums[i-1]:
                continue
            else:
                while left < right:
                    # print(right,left)
                    sum = val + nums[left] + nums[right]
                    if sum == 0:
                        res.append([val, nums[left],nums[right]])
                        left +=1
                        while nums[left] == nums[left-1] and left<right:
                            left+=1
                    else:
                        if sum>0:
                            right -=1
                        else:
                            left +=1
        return res
