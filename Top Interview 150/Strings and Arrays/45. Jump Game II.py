# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

 

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [2,3,0,1,4]
# Output: 2
 

# Constraints:

# 1 <= nums.length <= 104
# 0 <= nums[i] <= 1000
# It's guaranteed that you can reach nums[n - 1].


# #method 1: By beauty
# class Solution(object):
#     def jump(self, nums):
#         ln = len(nums)
#         final_pos = ln-1
#         total_jump = -1
#         highest_index = 0

#         for i in range(ln-1,-1,-1):
#             print(f"i:{i},final pos: {final_pos}")
#             if final_pos == i:
#                 smallest = final_pos
#                 for j in range(i-1,-1,-1):
#                     if j+nums[j] >= final_pos:
#                         print(f" j: {j} + val: {nums[j]} >= target: {final_pos}")
#                         print(i,j)
#                         if smallest>j:
#                             smallest = j
#                             # print(smallest)
#                             # final_pos = j
#                 if smallest<final_pos:
#                     final_pos = smallest
#                 total_jump +=1
#                 print(total_jump)
#         return total_jump
    
#method 2: from Youtube
# same approch from forward, instead of j loop here is sliding window
# explanation:
# within every steps max reach, i create a set of steps(window). for each window you consider that as a new step
# with that group of steps(window), what is the max i can reach
# update the max reach distance and create that as a next group of steps
# if i can reach destination with a group of steps, return true


class Solution(object):
    def jump(self, nums):
        coverage = nums[0]
        lastindex = 0
        total_jump = 0
        destination = len(nums)-1
        if len(nums) <2:
            return 0
        for i in range(0,len(nums)):
            coverage = max(coverage,nums[i]+i)
            if i == lastindex:
                lastindex = coverage
                print(coverage)
                total_jump += 1
                if (coverage >= destination):
                    return total_jump
        return total_jump



# nums = [2,4,1,2,3,1,1,2]
nums = [2,3,1,1,4]
s = Solution()
print(s.jump(nums))