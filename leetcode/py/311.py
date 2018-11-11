class Solution:
    """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """
    def multiply(self, A, B):
        row = len(A)
        col = len(B[0])
        res = [[0] * col for _ in range(row)]

        for i in range(row):
            for j in range(col):
                for k, n in enumerate(A[i]):
                    res[i][j] += n * B[k][j]

        return res
