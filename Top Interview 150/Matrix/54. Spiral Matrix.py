# Given an m x n matrix, return all elements of the matrix in spiral order.

 

# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:


# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100

# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# colBegin, rowBegin = 0, 0
# colEnd = len(matrix[0]) -1
# rowEnd = len(matrix) -1

# while colBegin <= colEnd and rowBegin <= rowEnd:
#     for i in range(colBegin,colEnd+1):
#         print(matrix[rowBegin][i])
#     rowBegin +=1
    
#     for i in range(rowBegin,rowEnd+1):
#         print(matrix[i][colEnd])
#     colEnd -=1
    
#     for i in range(colEnd,colBegin-1,-1):
#         print(matrix[rowEnd][i])
#     rowEnd -=1
    
#     for i in range(rowEnd, rowBegin-1, -1):
#         print(matrix[colBegin][i])
#     colBegin +=1


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        colBegin, rowBegin = 0, 0
        colEnd = len(matrix[0]) -1
        rowEnd = len(matrix) -1

        while colBegin <= colEnd and rowBegin <= rowEnd:
            for i in range(colBegin,colEnd+1):
                res.append(matrix[rowBegin][i])
            rowBegin +=1
            
            for i in range(rowBegin,rowEnd+1):
                res.append(matrix[i][colEnd])
            colEnd -=1
            
            if rowBegin <= rowEnd: 
                for i in range(colEnd,colBegin-1,-1):
                    res.append(matrix[rowEnd][i])
                rowEnd -=1

            if colBegin <= colEnd:            
                for i in range(rowEnd, rowBegin-1, -1):
                    res.append(matrix[i][colBegin])
                colBegin +=1
        return res
                
                
            