class UnionFind:
    def __init__(self, size):
        self.m = {i: i for i in range(size)}
        self.size = size

    def union(self, n1, n2):
        r1, r2 = self.find(n1), self.find(n2)
        if r1 != r2:
            self.size -= 1
            self.m[r1] = r2

    def find(self, n):
        if self.m[n] != n:
            self.m[n] = self.find(self.m[n])
        return self.m[n]

class Solution:
    def minMalwareSpread(self, graph, initial):
        M, N = len(graph), len(graph[0])

        uf = UnionFind(M)
        for i in range(M):
            for j in range(N):
                if graph[i][j] == 1:
                    uf.union(i, j)

        root_cnt_map = collections.Counter(uf.find(i) for i in range(M))
        initial_cnt_map = collections.Counter(uf.find(n) for n in initial)

        res = [(-root_cnt_map[uf.find(n)], n) for n in initial if initial_cnt_map[uf.find(n)] == 1]
        return min(res)[1] if res else min(initial)

