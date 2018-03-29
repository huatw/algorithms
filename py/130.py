class Solution:
    def solve(self, board):
        M, N = len(board), len(board[0])

        if M <= 2 or N <= 2:
            return

        def dfs(i, j):
            if i < 0 or j < 0 or i >= M or j >= N or board[i][j] != 'O':
                return

            board[i][j] = None

            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for i in range(N):
            dfs(0, i)
            dfs(N - 1, i)

        for i in range(M):
            dfs(i, 0)
            dfs(i, M - 1)

        for i in range(M):
            for j in range(N):
                if board[i][j] == None:
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'




# what ?? error ????
class Solution:
    def solve(self, board):
        def dfs(x, y):
            if board[x][y] == '?':
                return False

            if board[x][y] == 'X' or board[x][y] == None:
                return True

            if x == 0 or y == 0 or x == len(board) - 1 or y == len(board[0]) - 1:
                return False

            board[x][y] = None

            if dfs(x + 1, y) and dfs(x - 1, y) and dfs(x, y + 1) and dfs(x, y - 1):
                return True

            board[x][y] = '?'
            return False


        for x, row in enumerate(board[1: -1]):
            for y, el in enumerate(row[1: -1]):
                dfs(x + 1, y + 1)

        for x, row in enumerate(board[1: -1]):
            for y, el in enumerate(row[1: -1]):
                if not el:
                    board[x + 1][y + 1] = 'X'
                elif el == '?':
                    board[x + 1][y + 1] = 'O'



