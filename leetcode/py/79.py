class Solution:
    def exist(self, board, word):
        if not board or not board[0]:
            return False

        if not word:
            return True

        M, N = len(board), len(board[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def get_neighbors(x, y):
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if M > nx >= 0 and N > ny >= 0:
                    yield (nx, ny)

        def dfs(x, y, idx, seen):
            if (x, y) in seen or board[x][y] != word[idx]:
                return False
            if idx == len(word) - 1:
                return True
            seen.add((x, y))
            res = any(dfs(nx, ny, idx + 1, seen) for nx, ny in get_neighbors(x, y))
            seen.remove((x, y))
            return res

        return any(dfs(i, j, 0, set()) for i in range(M) for j in range(N))


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

        return any(search(x, y, word) for x, row in enumerate(board) for y, el in enumerate(row))
