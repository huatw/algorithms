class Solution:
    def spiralOrder(self, matrix):
        if not matrix:
            return []

        row_len, col_len = len(matrix), len(matrix[0])
        boundaries = (len(matrix), len(matrix[0]), 0, 0)
        updates = [(0, 0, 1, 0), (0, -1, 0, 0), (-1, 0, 0, 0), (0, 0, 0, 1)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cnt = 0
        res = []
        k = 0
        x, y = 0, -1
        i, j = directions[k]

        while cnt < row_len * col_len:
            n_x, n_y = x + i, y + j
            if boundaries[0] > n_x >= boundaries[2] and boundaries[1] > n_y >= boundaries[3]:
                res.append(matrix[n_x][n_y])
                cnt += 1
                x, y = n_x, n_y
            else:
                boundaries = tuple(b + u for b, u in zip(boundaries, updates[k]))
                k = (k + 1) % 4
                i, j = directions[k]

        return res
