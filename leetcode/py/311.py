class Solution:
    def multiply(self, A, B):
        row = len(A)
        col = len(B[0])
        res = [[0] * col for _ in range(row)]

        for i in range(row):
            for j in range(col):
                for k, n in enumerate(A[i]):
                    res[i][j] += n * B[k][j]

        return res




class Solution:
    def multiply(self, A, B):
        row = len(A)
        col = len(B[0])

        res = [[0] * col for _ in range(row)]

        for i in range(row):
            for k, n in enumerate(A[i]):
                if n:
                    for j in range(col):
                        if B[k][j]:
                            res[i][j] += n * B[k][j]

        return res

