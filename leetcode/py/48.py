'''
input:
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

output:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

left-top to right-bottom
x - y axis:
[
  [1,4,7],
  [2,5,8],
  [3,6,9]
]
y axis:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
'''
class Solution:
    def rotate(self, matrix):
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(len(matrix)):
            for j in range(len(matrix) // 2):
                matrix[i][j], matrix[i][len(matrix) - j - 1] = \
                  matrix[i][len(matrix) - j - 1], matrix[i][j]



