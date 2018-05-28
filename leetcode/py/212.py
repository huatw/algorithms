class Solution:
    def findWords(self, board, words):
        trie = {}
        ret = set()


        def dfs(x, y, t, path):
            if '$' in t:
                ret.add(path)

            if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]) or board[x][y] not in t:
                return

            temp = board[x][y]
            board[x][y] = None

            for dx, dy in ((0,1), (0,-1), (1,0), (-1,0)):
                dfs(x + dx, y + dy, t[temp], path + temp)

            board[x][y] = temp


        for word in words:
            t = trie
            for ch in word:
                if ch not in t:
                    t[ch] = {}
                t = t[ch]
            t['$'] = True

        for x, row in enumerate(board):
            for y, el in enumerate(row):
                dfs(x, y, trie, '')

        return list(ret)
