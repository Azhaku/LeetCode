# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.


# method-1(naive approach): time(O(m*n)) m-len(str[0]), n = len(str)
class Solution(object):
    def longestCommonPrefix(self, strs):
        string = ''
        for i in range(0,len(strs[0])):
            for j in range(1,len(strs)):
                if len(strs[j]) >= i+1:
                    if strs[0][i] == strs[j][i]:
                        continue
                    else:
                        return string
                else:
                    return string
            string += strs[0][i]
        return string

# method-2(sorting): time(O(n log n))
# sort the list and compare the first and last element
class Solution(object):
    def longestCommonPrefix(self, strs):
        string = ''
        strs = sorted(strs)
        first = strs[0]
        last = strs[-1]
        for i in range(min(len(first),len(last))):
            if first[i] == last[i]:
                string += first[i]
            else:
                break
        return string



s =Solution()
# test case 1
strs = ["flower","flow","flight"]
assert 'fl' == s.longestCommonPrefix(strs)
# test case 2
strs1 = ["dog","racecar","car"]
assert '' == s.longestCommonPrefix(strs1)
