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