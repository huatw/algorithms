'''
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
'''
class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        k = -1

        for row in matrix:
            while len(row) + k > 0 and row[k] > target:
                k -= 1
            if row[k] == target:
                return True

        return False