class Solution:
    def generate(self, num_rows):
        if num_rows == 0:
            return []
        res = []
        for level_len in range(1, num_rows + 1):
            level = [1] * level_len
            for i, num in enumerate(level[1:-1]):
                level[i + 1] = res[-1][i + 1] + res[-1][i]
            res.append(level)
        return res

class Solution:
    def generate(self, numRows):
        if numRows == 0:
            return []

        res = [[1]]

        for _ in range(numRows - 1):
            row = [*res[-1], 0]
            for i in range(len(row) - 1, -1, -1):
                row[i] = 1 if i == 0 else row[i] + row[i - 1]

            res.append(row)

        return res