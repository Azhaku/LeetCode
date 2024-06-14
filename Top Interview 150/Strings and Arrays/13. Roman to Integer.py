# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

 

# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

# Constraints:

# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].

# Hard coding: with 0(n)time(beats 65%), 0(1) space(beats(99%))
# class Solution(object):
#     def romanToInt(self, s):
#         dic = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
#         number = 0
#         i=0
#         while i<len(s):
#             if i < len(s)-1:
#                 if s[i] =="I":
#                     if s[i+1] in["X","V"]:
#                         number += dic[s[i+1]] - dic['I']
#                         i += 2
#                     else:
#                         number += dic[s[i]]
#                         i +=1
#                 elif s[i] == "X":
#                     if s[i+1] in ["L","C"]:
#                         number += dic[s[i+1]] - dic['X']
#                         i += 2
#                     else:
#                         number += dic[s[i]]
#                         i +=1

#                 elif s[i] == "C":
#                     if s[i+1] in ["D","M"]:
#                         number += dic[s[i+1]] - dic["C"]
#                         i+=2
#                     else:
#                         number += dic[s[i]]
#                         i +=1
#                 else:
#                     number += dic[s[i]]
#                     i +=1

#             else:
#                 number += dic[s[i]]
#                 i +=1
#         return number

# # method - 2: two pointer(56%,92%)
class Solution(object):
    def romanToInt(self, s):
        dic = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        number = 0
        i=0
        n = len(s)
        for i in range(0,n-1):
            if dic[s[i]]<dic[s[i+1]]:
                number -= dic[s[i]]
            else:
                number += dic[s[i]]
        number += dic[s[n-1]]
        return number

# method 3: (change the input values) time(beats 75%),space(beats 82%)
# class Solution:
#     def romanToInt(self, s):
#         dic = {
#             'I': 1,
#             'V': 5,
#             'X': 10,
#             'L': 50,
#             'C': 100,
#             'D': 500,
#             'M': 1000,
#         }
#         number = 0
#         s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
#         for char in s:
#             number += dic[char]
#         return number
    
s = Solution()
ip = "IXXCCDCM" # (IX) = 9, (XC) = 90, "CD" = 400, "CM" = 900, Total = 900+400+90+9
assert 1399 == s.romanToInt(ip)
print(s.romanToInt(ip))