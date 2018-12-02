'''
Given matrix = [
  [3, 1],
  [5, 6],
]
[
    [0, 0, 0],
    [0, 3, 4],
    [0, 5, 11],
]
[
    [0, 0, 0],
    [0, 3, 4],
    [0, 8, 15],
]
'''
class NumMatrix:
    def __init__(self, matrix):
        if not matrix or not matrix[0]:
            self.totals = [[0]]
            return

        self.totals = [[0] * (len(matrix[0]) + 1)]
        for row in matrix:
            self.totals.append([0])
            for num in row:
                self.totals[-1].append(self.totals[-1][-1] + num)
        for i, row in enumerate(self.totals):
            if i == 0:
                continue
            for j, num in enumerate(row):
                self.totals[i][j] += self.totals[i - 1][j]

    def sumRegion(self, row1, col1, row2, col2):
        return self.totals[row2 + 1][col2 + 1] + self.totals[row1][col1] - self.totals[row1][col2 + 1] - self.totals[row2 + 1][col1]