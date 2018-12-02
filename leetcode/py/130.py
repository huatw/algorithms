class Solution:
    def solve(self, board):
        if not board or not board[0]:
            return

        M, N = len(board), len(board[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        def get_neighbors(x, y):
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if M > nx >= 0 and N > ny >= 0:
                    yield (nx, ny)

        def dfs(x, y):
            if board[x][y] == 'O':
                board[x][y] = None
                for nx, ny in get_neighbors(x, y):
                    dfs(nx, ny)

        for i in range(M):
            dfs(i, 0)
            dfs(i, N - 1)

        for j in range(N):
            dfs(0, j)
            dfs(M - 1, j)

        for i in range(M):
            for j in range(N):
                if board[i][j] == None:
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'





class Solution:
    def solve(self, board):
        if not board or not board[0]:
            return
        M, N = len(board), len(board[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        def dfs(x, y):
            if not (M > x >= 0 and N > y >= 0 and board[x][y] == 'O'):
                return
            board[x][y] = '#'
            for (dx, dy) in DIRECTIONS:
                dfs(x + dx, y + dy)

        for i in range(M):
            dfs(i, 0)
            dfs(i, N - 1)

        for i in range(N):
            dfs(0, i)
            dfs(M - 1, i)

        for i in range(M):
            for j in range(N):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
