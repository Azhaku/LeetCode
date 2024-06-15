# You are given a string s and an array of strings words. All the strings of words are of the same length.

# A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

# For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
# Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

 

# Example 1:

# Input: s = "barfoothefoobarman", words = ["foo","bar"]

# Output: [0,9]

# Explanation:

# The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
# The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

# Example 2:

# Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

# Output: []

# Explanation:

# There is no concatenated substring.

# Example 3:

# Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

# Output: [6,9,12]

# Explanation:

# The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
# The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
# The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].

 

# Constraints:

# 1 <= s.length <= 104
# 1 <= words.length <= 5000
# 1 <= words[i].length <= 30
# s and words[i] consist of lowercase English letters.



# # Not working : random approach with two pointer
# class Solution(object):
#     def findSubstring(self, s, words):
#         alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#         indices_a = [0]*26
#         indices_b = [0]*26
#         indices_c = []
#         string = "".join(words)
#         res = []
#         for c in string:
#             i = alpha.index(c)
#             indices_b[i] += 1
#         # print(indices)
#         # for i in range(0,len(s)-(len(string)-1),len(words[0])):
#         l = 0
#         r = len(s) - (len(string)) 
#         while l < r:
#             indices_c = list(indices_b)
#             print(indices_b)
#             # print(s[i])
#             for f in words:
#                 if s[l] == f[0]:
#                     break
#                 else:
#                     l+=1

#             for j in range(l,l+len(string)):
#                 print(l,s[l],l+len(string)-1,s[l+len(string)-1])
#                 if indices_c[alpha.index(s[j])] > 0:
#                     ind = alpha.index(s[j])
#                     indices_c[ind] -=1
#                 else:
#                     break
#             if indices_c == indices_a:
#                 res.append(l)
#                 l +=len(words[0])
#             else:
#                 l +=1
#         return res


#method - 2(sliding window, )
class Solution(object):
    def findSubstring(self, s, words):
        
        l = len(words[0])
        dic = {}
        for word in words:
            if word in dic:
                dic[word] += 1
            else:
                dic[word] = 1
        
        res = []
        print(l)
        #sliding windows
        for i in range(l):
            left = i
            subdic = {}
            count = 0

            for j in range(i,len(s)-l+1, l):
                tword = s[j:j+l]

                #valid word
                if tword in dic:

                    if tword in subdic:
                        subdic[tword]+=1
                    else:
                        subdic[tword] = 1

                    count +=1

                    # when a word appear more than we know, we remove the previous words untill,
                    #   it is less than or equal to the original word freq.
                    #   eg:["wordgoodgoodgoodbestword"]
                    while subdic[tword] > dic[tword]:
                        print(subdic,dic,tword)
                        subdic[s[left:left+l]] -=1
                        left+=l
                        count -=1

                    # print(tword)
                    # append words when all words were found
                    if count == len(words):
                        res.append(left)

                #not valid
                else:
                    left = j+l
                    subdic = {}
                    count = 0
        return res          