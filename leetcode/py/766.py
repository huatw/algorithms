'''
matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
'''
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        if not matrix or not matrix[0]:
            return True

        for i, row in enumerate(matrix):
            for j, item in enumerate(row):
                if i > 0 and j > 0 and item != matrix[i - 1][j - 1]:
                    return False

        return True
