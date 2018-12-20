# DFS
class Solution:
    def calcEquation(self, equations, values, queries):
        from_to_map = collections.defaultdict(collections.defaultdict)

        for (f, t), ratio in zip(equations, values):
            from_to_map[f][t] = ratio
            from_to_map[t][f] = 1 / ratio

        def query(f, t, seen):
            if  f in seen or f not in from_to_map or t not in from_to_map:
                return -1.0
            seen.add(f)
            if f == t:
                return 1.0
            for next_f, ratio in from_to_map[f].items():
                next_ratio = query(next_f, t, seen)
                if next_ratio != -1.0:
                    return next_ratio * ratio
            seen.remove(f)
            return -1.0

        return [query(f, t, set()) for (f, t) in queries]




# Union Find
class UnionFind:
    def __init__(self):
        self.m = {}

    def union(self, f, t, ratio):
        if f not in self.m:
            self.m[f] = (f, 1.0)
        if t not in self.m:
            self.m[t] = (t, 1.0)
        (r1, ratio1), (r2, ratio2) = self.find(f), self.find(t)
        if r1 != r2:
            self.m[r1] = r2, ratio * ratio2 / ratio1

    def find(self, n):
        p, p_ratio = self.m[n]
        if p != n:
            r, r_ratio = self.find(p)
            self.m[n] = r, r_ratio * p_ratio
        return self.m[n]

    def query(self, f, t):
        if f not in self.m or t not in self.m:
            return -1.0
        if f == t:
            return 1.0
        (r1, ratio1), (r2, ratio2) = self.find(f), self.find(t)
        return ratio1 / ratio2 if r1 == r2 else -1.0

class Solution:
    def calcEquation(self, equations, values, queries):
        uf = UnionFind()
        for (f, t), ratio in zip(equations, values):
            uf.union(f, t, ratio)
        return [uf.query(f, t) for f, t in queries]
