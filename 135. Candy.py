# There are n children standing in a line. Each child is assigned a ratings value given in the integer array ratings.

# You are giving candies to these children subjected to the following requirements:

# Each child must have at least one candy.
# Children with a higher ratings get more candies than their neighbors.
# Return the minimum number of candies you need to have to distribute the candies to the children.

 

# Example 1:

# Input: ratings = [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
# Example 2:

# Input: ratings = [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
# The third child gets 1 candy because it satisfies the above two conditions.
 

# Constraints:

# n == ratings.length
# 1 <= n <= 2 * 104
# 0 <= ratings[i] <= 2 * 104

# ratings = [1,0,2]
# ratings = [1,2,87,87,87,2,1]
ratings = [1,3,2,2,1]
def candy( ratings):
    left= [1 for i in range(len(ratings))]
    right = [1 for i in range(len(ratings))]
    for i in range(1,len(ratings)):
        if ratings[i-1]<ratings[i]:
            right[i] = right[i-1]+1
    for i in range(len(ratings)-2,-1,-1):
        if ratings[i]>ratings[i+1]:
            left[i] = left[i+1]+1
    candy = 0
    for i in range(len(right)):
        candy += max(right[i],left[i])
    return candy
                

print(candy(ratings))
