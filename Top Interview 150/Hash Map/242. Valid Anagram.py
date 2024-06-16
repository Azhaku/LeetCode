# Given two strings s and t, return true if t is an anagram of s, and false otherwise.


# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
 
 # method 1: time O(n)
class Solution(object):
    def isAnagram(self, s, t):
        s_dic = {}
        
        # if length not equal can't be anagram
        if len(s) != len(t):
            return False
        
        #create freq dic
        for i in s:
            if i in s_dic:
                s_dic[i] +=1
            else:
                s_dic[i] = 1
        
        for j in t:
            # check whether it have a same chars as s
            if j in s_dic and s_dic[j] > 0:
                s_dic[j] -= 1
                # print(s_dic)
            else:
                return False
        return True
        
# method 2: time O(nlogn)
class Solution(object):
    def isAnagram(self,s,t):
        
        #create sorted char array
        s = sorted(s) 
        t = sorted(t)
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if s[i]!= t[i]:
                return False
        return True    
        
            
s = "anagram"
t = "nagaram" 
S = Solution()
print(S.isAnagram(s,t))
