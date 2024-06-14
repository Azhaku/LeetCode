# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
 

# Constraints:

# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
# 0 <= k <= 105
 

# Follow up:

# Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
# Could you do it in-place with O(1) extra space?

nums = [1,2,3,4,5,6,7]
k = 3


# // method 1 Brute force O(n)
# for i in range(0,k):
#     last_element = nums.pop()
#     nums.insert(0,last_element)
#     print(nums)


# // Method 2 O(1)

if len(nums)<2:
    return nums
if k<=0:
    return nums
if k > len(nums):
    k = k%len(nums)
half_2 = nums[:-k]
half_1= nums[-k:]
nums[:k] = half_1 
nums[k:] = half_2
return nums
