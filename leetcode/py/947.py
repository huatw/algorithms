class UnionFind:
    def __init__(self):
        self.m = {}
        self.size = 0

    def union(self, row, col):
        row, col = (row, None), (None, col)
        if row not in self.m:
            self.m[row] = row
            self.size += 1
        if col not in self.m:
            self.m[col] = col
            self.size += 1
        r1, r2 = self.find(row), self.find(col)
        if r1 != r2:
            self.size -= 1
            self.m[r1] = r2
    def find(self, rc):
        if self.m[rc] != rc:
            self.m[rc] = self.find(self.m[rc])
        return self.m[rc]

class Solution:
    def removeStones(self, stones):
        uf = UnionFind()
        for x, y in stones:
            uf.union(x, y)
        return len(stones) - uf.size



# DFS
class Solution:
    def removeStones(self, stones):
        row_cols_map = collections.defaultdict(list)
        col_rows_map = collections.defaultdict(list)
        seen_row, seen_col = set(), set()
        n_connected = 0

        def dfs_row(row):
            if row in seen_row:
                return
            seen_row.add(row)
            for col in row_cols_map[row]:
                dfs_col(col)

        def dfs_col(col):
            if col in seen_col:
                return
            seen_col.add(col)
            for row in col_rows_map[col]:
                dfs_row(row)

        for row, col in stones:
            row_cols_map[row].append(col)
            col_rows_map[col].append(row)

        for row in row_cols_map.keys():
            if row not in seen_row:
                n_connected += 1
                dfs_row(row)

        return len(stones) - n_connected

