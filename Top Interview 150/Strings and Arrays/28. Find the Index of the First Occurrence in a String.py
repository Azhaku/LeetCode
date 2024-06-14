# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

# Constraints:

# 1 <= haystack.length, needle.length <= 104
# haystack and needle consist of only lowercase English characters.

# method -1 , worst case O(n*m)


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        tar_len = len(needle)

        for i in range(len(haystack)-(tar_len-1)):
            count =0
            if haystack[i] == needle[0]:
                for j in range(tar_len):
                    if haystack[j+i] != needle[j]:
                        break
                    else:
                        count+=1
                    if count == tar_len:
                        return i
        return -1