class Solution:
    def candyCrush(self, board):
        rotate_90 = lambda board: list(map(list, zip(*reversed(board))))
        rotate_n90 = lambda board: list(reversed(list(map(list, zip(*board)))))
        board = rotate_90(board)
        M, N = len(board), len(board[0])

        while True:
            remove_set = set()
            for i in range(M):
                for j in range(2, N):
                    if board[i][j] and board[i][j] == board[i][j - 1] == board[i][j - 2]:
                        remove_set = remove_set.union([(i, j), (i, j - 1), (i, j - 2)])
            for j in range(N):
                for i in range(2, M):
                    if board[i][j] and board[i][j] == board[i - 1][j] == board[i - 2][j]:
                        remove_set = remove_set.union([(i, j), (i - 1, j), (i - 2, j)])
            if not remove_set:
                break
            for i, j in remove_set:
                board[i][j] = 0
            for i in range(M):
                row = [v for v in board[i] if v != 0]
                board[i] = row + (N - len(row)) * [0]

        return rotate_n90(board)



class Solution:
    def candyCrush(self, board):
        # rotate clockwise 90 degree
        board = list(map(list, zip(*reversed(board))))
        M, N = len(board), len(board[0])
        # repeat crush and drop
        while True:
            candy = set()
            # check every row
            for i in range(M):
                for j in range(2, N):
                    if board[i][j] and board[i][j] == board[i][j - 1] == board[i][j - 2]:
                        candy = candy.union([(i, j), (i, j - 1), (i, j - 2)])

            # check every col
            for j in range(N):
                for i in range(2, M):
                    if board[i][j] and board[i][j] == board[i - 1][j] == board[i - 2][j]:
                        candy = candy.union([(i, j), (i - 1, j), (i - 2, j)])

            if not candy:
                break

            for i, j in candy:
                board[i][j] = 0

            # drop the board, move non-zero to the beginning of each row.
            for i in range(M):
                row = [v for v in board[i] if v != 0]
                board[i] = row + [0] * (N - len(row))

        # rotate counter-clockwise 90 degree
        board = list(reversed(list(map(list, zip(*board)))))
        return board
