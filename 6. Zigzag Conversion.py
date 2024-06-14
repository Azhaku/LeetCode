# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);
 

# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# Example 3:

# Input: s = "A", numRows = 1
# Output: "A"

class Solution(object):
    def convert(self, s, numRows):
        n = len(s)
        ans = ""
        if numRows==1:
            return s
        increment = 2*(numRows -1)
        for row in range(numRows):
            for i in range(row,n,increment):
                ans += s[i]
                if (row > 0 and row<numRows-1 and i+increment - 2*row < n):
                    ans += s[i+increment - 2*row]
        return ans
                
