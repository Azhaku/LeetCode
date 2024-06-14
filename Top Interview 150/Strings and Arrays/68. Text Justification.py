# Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

# You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

# Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

# For the last line of text, it should be left-justified, and no extra space is inserted between words.

# Note:

# A word is defined as a character sequence consisting of non-space characters only.
# Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
# The input array words contains at least one word.
 

# Example 1:

# Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
# Output:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
# Example 2:

# Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
# Output:
# [
#   "What   must   be",
#   "acknowledgment  ",
#   "shall be        "
# ]
# Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
# Note that the second line is also left-justified because it contains only one word.
# Example 3:

# Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
# Output:
# [
#   "Science  is  what we",
#   "understand      well",
#   "enough to explain to",
#   "a  computer.  Art is",
#   "everything  else  we",
#   "do                  "
# ]
 
# still have some bug
# class Solution:
#     def justify(self,line,maxWidth,cur_size):
#         s = ""
#         if len(line) == 1:
#             return line[0] + " "*(maxWidth - cur_size)
#         else:
#             space = maxWidth - cur_size
#             evenSpace = space//(len(line)-1)
#             remainingSpace = space% (len(line)-1)
#             for i in range(len(line)-1):
#                 s += line[i] + " "
#                 s += " "*evenSpace
#                 if remainingSpace>0:
#                     s += " "
#                     remainingSpace -=1
#             s += line[-1]
#         return s
        
    
#     def fullJustify(self, words, maxWidth) :
#         left = 0
#         cur_size = 0
#         word_count = 0
#         res_list = []
#         line = []
#         for word in words:
#             cur_size+=len(word) + 1
#             if cur_size <= maxWidth:
#                 print(cur_size)
#                 line.append(word)
#             else:
#                 res_list.append(self.justify(line,maxWidth,cur_size))
#                 cur_size = len(word)+1
#                 line = [word]
#         if word == line[-1]:
#             res_list.append(self.justify(line,maxWidth,cur_size))
               
#             print(line,cur_size)
#         return res_list

# s = Solution()
words = ["This", "is", "an", "example", "of", "text", "justification."]
# words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
# for i in words[:-2]:
#     print(i)
maxWidth = 16
# print(s.fullJustify(words,maxWidth))
s = "0P"
low = s.lower()
print(low)
if ord(s[0])>47 and ord(s[0])<58:
    print(True)