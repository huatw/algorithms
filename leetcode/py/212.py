class Solution:
    def findWords(self, board, words):
        M, N = len(board), len(board[0])
        def get_neighbors(x, y):
            DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if M > nx >= 0 and N > ny >= 0:
                    yield (nx, ny)

        def build_trie(words):
            trie = {}
            for word in words:
                node = trie
                for ch in word:
                    if ch not in node:
                        node[ch] = {}
                    node = node[ch]
                node['$'] = True
            return trie

        def dfs(x, y, node, path, seen):
            if (x, y) in seen:
                return
            seen.add((x, y))
            for next_ch, next_node in node.items():
                if board[x][y] == next_ch:
                    path.append(next_ch)
                    if '$' in next_node:
                        yield ''.join(path)
                    for nx, ny in get_neighbors(x, y):
                        yield from dfs(nx, ny, next_node, path, seen)
                    path.pop()
            seen.remove((x, y))

        trie = build_trie(words)
        return list(set(word for i in range(M) for j in range(N) for word in dfs(i, j, trie, [], set())))
