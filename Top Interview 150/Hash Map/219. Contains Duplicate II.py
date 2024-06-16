# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
 

# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
# 0 <= k <= 105

# method 1: without hashtable

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        l = 0
        for r in range(0,len(nums)):
            if (r-l) > k:
                l+= 1
            if nums[r] in nums[l:r]:
                return True
        return False
        
        
# method 2: using hashtable
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        dict1 = {}
        for idx,val in enumerate(nums):

            #check val in dic and index of previous val and current val in less k window
            if val in dict1 and abs(idx-dict1[val])<=k:
                return True
            else:
                #store the seen value and index
                dict1[val]=idx
        
        return False
        
# method 3: using hashset
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        window = set()
        l = 0
        for r in range(0,len(nums)):
            if (r-l) > k:
                window.remove(nums[l])
                l+= 1
            if nums[r] in window:
                return True
            window.add(nums[r])
        return False
        