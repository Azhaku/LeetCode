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
class Solution(object):
    def reverseWords(self, s):
        left = 0
        right = 0
        s = list(s)
        n = len(s)
        i = 0
        def rever(s,start,end):
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1

        while i<n:
            while (i<n and s[i]== ' '):
                i += 1
            if i==n:
                break
            while (i<n and s[i]!= ' '):
                s[right] = s[i]
                i +=1
                right +=1
            rever(s,left,right-1)
            if right<n:
                s[right] = " "
            right +=1
            left = right
            i+=1
        s = "".join(s[:right-1][::-1])
        return s
s = "the sky is blue"
s1 = Solution()
print(s1.reverseWords(s))
