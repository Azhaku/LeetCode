# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]
 

# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

# method 1: works good but still can be optimized

class Solution(object):
    def groupAnagrams(self, strs):
        dic = {}
        for s in strs:
            
            # get ssorted chars to identify anagrams
            ns = "".join(sorted(s))
            
            if ns in dic.keys():
                dic[ns] += [s]
            else:
                dic[ns] = [s]
                
        return list(dic.values())
    
# same as method 1, little bit better
class Solution(object):
    def groupAnagrams(self, strs):
        dic = defaultdict(list)
        # print(dic)
        for s in strs:
            ns = "".join(sorted(s))
            dic[ns].append(s)
        return dic.values()



strs = ["eat","tea","tan","ate","nat","bat"]
s = Solution()
print(s.groupAnagrams(strs))