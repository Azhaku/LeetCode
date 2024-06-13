# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
 
 # method 1: brute force - O(n)time, O(n)space
 class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        left = 0
        new_s = ''
        for i in s:
            print(i)
            is_alpha = (97 <= ord(i)) and (ord(i)<= 122)
            if (is_alpha) or (47<ord(i) and ord(i)<58):
                new_s +=i
        right = len(new_s) - 1
        if len(new_s) == 0:
            return True
        while left<= right:
            if new_s[left] == new_s[right]:
                left +=1
                right -=1
            else: return False
        return True


class Solution(object):
    def isPalindrome(self, s):
        s = s.lower() #if space needs to be optimized add conditions to check upper char also. and while comparing use .lower() for each char
        left = 0
        right = len(s)-1
        if len(s) == 0:
            return True
        while left<right:
            # print(left,right)
            while left<right and not((97 <= ord(s[left]) <= 122) or (47 < ord(s[left]) < 58)):
                # print(left)
                left += 1
            while left<right and not((97 <= ord(s[right]) <= 122) or (47 < ord(s[right]) < 58)) :
                right -= 1
            if s[left] == s[right]:
                # print(s[left],s[right])
                left +=1
                right -=1
            else: 
                return False
        return True
        