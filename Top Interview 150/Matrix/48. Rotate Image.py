from typing import List
matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[5,1,9,11,],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
length = len(matrix[0])
max = length-1
start = 0

    
for i in range(0,length-2):
    for j in range(i,(length - (i+1))):
        
        # print(matrix[start][max - j])
        # print(matrix[max-j][start])
        # print(matrix[max][max-j])
        # print(matrix[start+j][max])
        temp = matrix[start+i][max - j]
        matrix[start+i][max - j] = matrix[j+start][start+i]
        matrix[j+start][start+i] = matrix[max - i][j]
        matrix[max - i][j] = matrix[max-j][max - i]
        matrix[max-j][max - i] = temp


class Solution(object):
    def rotate(self, matrix):
        length = len(matrix[0])
        max = length-1
        start = 0  
        for i in range(0,length-1):
            for j in range(i,(length - (i+1))):
                
                # save the top left value
                temp = matrix[start+i][max - j]
                
                # update the top left with bottom left
                matrix[start+i][max - j] = matrix[j+start][start+i]
                
                # update the bottom left with bottom right
                matrix[j+start][start+i] = matrix[max - i][j]
                
                # update the bottom right with top right
                matrix[max - i][j] = matrix[max-j][max - i]

                # update the top right with top left value
                matrix[max-j][max - i] = temp

        return matrix
    
    
# method - 2
def rotate(self, matrix: List[List[int]]) -> None:
    # First, reverse the matrix rows (flip the matrix vertically)
    matrix.reverse()
    
    # Now, transpose the matrix (swap rows with columns)
    n = len(matrix)
    for i in range(n):
        for j in range(i+1, n):  # Note: Starting from `i+1` to avoid redundant swaps
            # Swap matrix[i][j] and matrix[j][i]
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]