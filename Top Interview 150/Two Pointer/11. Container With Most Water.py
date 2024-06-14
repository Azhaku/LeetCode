# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most current_container .

# Return the maximum amount of current_container  a container can store.

# Notice that you may not slant the container.

 

# Example 1:


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of current_container  (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1
 

# Constraints:

# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104
class Solution(object):
    def maxArea(self, height):
        l = 0
        r = len(height)-1
        current_container  = 0
        biggest_container  = 0
        count = len(height)
        while l<r:
            count-=1
            current_container  = count* min(height[l], height[r])
            if current_container >biggest_container :
                biggest_container  = current_container 
            if height[r] > height[l]:
                l+=1
            else:
                r-=1

        return biggest_container 
    
nums = [2,3,4,5,6]
print(nums[:len(nums)])