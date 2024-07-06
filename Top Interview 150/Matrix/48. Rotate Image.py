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

                temp = matrix[start+i][max - j]
                matrix[start+i][max - j] = matrix[j+start][start+i]
                matrix[j+start][start+i] = matrix[max - i][j]
                matrix[max - i][j] = matrix[max-j][max - i]
                matrix[max-j][max - i] = temp

        return matrix