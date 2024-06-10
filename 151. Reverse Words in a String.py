# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

# Example 1:

# Input: s = "the sky is blue"
# Output: "blue is sky the"
# Example 2:

# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
# Example 3:

# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

# Constraints:

# 1 <= s.length <= 104
# s contains English letters (upper-case and lower-case), digits, and spaces ' '.
# There is at least one word in s.

# method -1(naive approach) O(n)-time, space-O(n)
class Solution(object):
    def reverseWords(self, s):
        s = s.strip().split()
        string = ''
        for i in range(len(s)-1,0,-1):
            string += s[i] + " "
        return string+s[0]
    
class Solution(object):
    def reverseWords(self, s):
        s = s.strip().split()[::-1]
        s = " ".join(s)
        return s
  
s = Solution()
# print(s.reverseWords("I am here"))  
# method -2(two pointer) O(n*m)-time[m-half(no.of chars)], space-O(1)
def reverse_words(s):
    left = 0
    i = 0
    s = list(" ".join(s.strip().split()))
    n = len(s)
    print(s)
      
    while(s[i] == ' '):
        i = i+1
    
    left = i
     
    while(i < n):
        if(i+1 == n or s[i] == ' '):
            right = i-1
            if i+1 == n:
                right = right+1
            # print(j)
             
            while left < right:
                s[left], s[right] = s[right], s[left]
                left = left+1
                right = right-1
             
            left = i + 1
        
         
        if(i > left and s[left] == ' '):
            print(i)
            left = i
         
        i = i+1
    s = ''.join(s)
    s = s[::-1]
    return s
 
s = "    here am    i   "
print(reverse_words(s))