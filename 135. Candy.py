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

ratings = [1,2,87,87,87,2,1]
# ratings = [1,3,2,2,1]
# def candy( ratings):
#     left= [1 for i in range(len(ratings))]
#     right = [1 for i in range(len(ratings))]
#     for i in range(1,len(ratings)):
#         if ratings[i-1]<ratings[i]:
#             right[i] = right[i-1]+1
#     for i in range(len(ratings)-2,-1,-1):
#         if ratings[i]>ratings[i+1]:
#             left[i] = left[i+1]+1
#     candy = 0
#     for i in range(len(right)):
#         candy += max(right[i],left[i])
#     return candy
                
#method 2: from Youtube
# ratings = [1,2]
# def candy(r):
#     up = 0
#     down = 0
#     candies = 1
#     last_max = 0
#     for prev,cur in zip(r[:-1],r[1:]):
#         # print(cur,prev)
#         if cur > prev:
#             up+=1
#             down = 0
#             last_max = up + 1
#             candies += 1+up
#         elif prev > cur:
#             down += 1
#             up = 0
#             if last_max <= down:
#                 # print(last_max,"<=",down)
#                 # print(prev,">",cur)
#                 candies+=1
#             candies += down
#         else:
#             up,down,last_max = 0,0,0
#             candies+=1
#     return candies
            
# print(candy(ratings))

#enhanced method 2:

def candy(r):
    up = 0
    down = 0
    candies = 1
    last_max = 0
    for i in range(1,len(r)):
        # print(cur,prev)
        if r[i] > r[i-1]:
            up+=1
            down = 0
            last_max = up + 1
            candies += 1+up
        elif r[i-1] > r[i]:
            down += 1
            up = 0
            if last_max <= down:
                # print(last_max,"<=",down)
                # print(prev,">",cur)
                candies+=1
            candies += down
        else:
            up,down,last_max = 0,0,0
            candies+=1
    return candies

r = [1,2,2,4,3,2,1]
print(candy(r))
