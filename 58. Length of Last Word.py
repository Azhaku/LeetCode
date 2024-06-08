# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal 
# substring
#  consisting of non-space characters only.

 

# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:

# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.
 

# Constraints:

# 1 <= s.length <= 104
# s consists of only English letters and spaces ' '.
# There will be at least one word in s.

# method 1:
# class Solution(object):
#    def lengthOfLastWord(self, s):
#        return len(s.strip().split()[-1])
    
# method 2:
class Solution(object):
    def lengthOfLastWord(self, s):
        count = 0
        for i in reversed(s):
#         for i in range(len(s)-1,-1,-1):
            if(i != " "):
                count += 1
            else:
                if count>0:
                    return count
        return count

    
s = Solution()
print(s.lengthOfLastWord("a"))
