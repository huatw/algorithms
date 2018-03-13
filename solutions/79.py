# DFS
class Solution:
    def exist(self, board, word):
        def search(x, y, rest):
            if not rest:
                return True
            if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]) or rest[0] != board[x][y]:
                return False

            temp = board[x][y]
            board[x][y] = None

            if search(x-1, y, rest[1:]) or search(x+1, y, rest[1:]) or search(x, y-1, rest[1:]) or search(x, y+1, rest[1:]):
                return True

            board[x][y] = temp
            return False

        for x, row in enumerate(board):
            for y, el in enumerate(row):
                if search(x, y, word):
                    return True

        return False
