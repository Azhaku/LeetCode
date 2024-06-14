# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

# # method-1: using extra space(set)
# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         sub_set = set()
#         left = 0
#         res = 0
#         for end in range(len(s)):
#             while s[end] in sub_set:
#                 sub_set.remove(s[left])
#                 left +=1
#             sub_set.add(s[end])
#             res = max(res, end - left +1)
#         return res

#method-2: without extra space time O(n), space O(1)
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        longest = 0
        count = 0
        start = 0

        for end in range(0,len(s)):
            if s[end] in s[start:end]:
                while s[end] in s[start:end]:
                    count = ((end-1) - start)+1
                    # print(end,start)
                    if count > longest:
                        longest = count
                    start += 1
            else:
                count = end - start +1
        if count>longest:
            return count
        else:
            return longest


        

        