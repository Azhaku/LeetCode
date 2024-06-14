# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.



# Example 1:


# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9
 

# Constraints:

# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105

# use two pointer method:
# first step: either right or left, iterate untill you find the bigger piller than it is on other side. when right and left crosses stop iterating
# second step: take the min piller from two side and subtract it with the current value to find the current place's water capacity then do increment/decrement
# third step: if you find the biggest piller on one side than its previous, reset the bigger piller value and repeat from step 1

# Optimal solution: time complexity:O(n), space complexity:O(1)
class Solution(object):
    def trap(self, h):
        water = 0
        n = len(h)
        left = 0
        right = n-1
        left_support = h[0]
        right_support = h[n-1]
        while(left <= right):
            if left_support < right_support:
                if h[left] > left_support:
                    left_support = h[left]
                else:
                    water += left_support - h[left] 
                    left +=1
            else:
                if h[right] > right_support:
                    right_support = h[right]
                else:
                    water += right_support - h[right]
                    right -= 1
                
                
        return water


h = [0,1,0,2,1,0,1,3,2,1,2,1]
s = Solution()
result = 6
assert result == s.trap(h)