# one pass
class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        dp = []

        for x, row in enumerate(matrix):
            dp.append([])
            for y, item in enumerate(row):
                dp[x].append((min(dp[x-1][y], dp[x][y-1], dp[x-1][y-1]) + 1 if x>0 and y>0 else 1)
                    if item == '1' else 0
                )

        maxV = max([max(row) for row in dp]) if matrix else 0

        return maxV ** 2

# two pass
class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0

        rowN, colN = len(matrix), len(matrix[0])
        dp = [[1 if item == '1' else 0 for item in row] for row in matrix]

        for x in range(1, rowN):
            for y in range(1, colN):
                if dp[x][y] == 1:
                    dp[x][y] = min(dp[x-1][y], dp[x][y-1], dp[x-1][y-1]) + 1

        maxV = max([max(row) for row in dp])

        return maxV ** 2
