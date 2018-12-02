# UF
class UnionFind:
    def __init__(self):
        self.m = {}
    def add(self, n1, n2):
        if n1 in self.m:
            self.m[n2] = n1
        elif n2 in self.m:
            self.m[n1] = n2
        else:
            self.m[n1] = n2
            self.m[n2] = n2
        return True
    def add_union(self, n1, n2):
        if n1 in self.m and n2 in self.m:
            return self.union(n1, n2)
        return self.add(n1, n2)
    def union(self, n1, n2):
        r1, r2 = self.find(n1), self.find(n2)
        if r1 == r2:
            return False
        self.m[r1] = r2
        return True
    def find(self, n):
        if self.m[n] != n:
            self.m[n] = self.find(self.m[n])
        return self.m[n]

class Solution:
    def findRedundantDirectedConnection(self, edges):
        def has_cycle(end_start_map, start, end):
            while start in end_start_map:
                start = end_start_map[start]
                if end == start:
                    return True
            return False

        candidates = []
        end_start_map = {}
        for (start, end) in edges:
            if end in end_start_map:
                candidates.append((end_start_map[end], end))
                candidates.append((start, end))
            else:
                end_start_map[end] = start
        if candidates:
            return candidates[0] if has_cycle(end_start_map, *candidates[0]) else candidates[1]

        uf = UnionFind()
        for (start, end) in edges:
            if not uf.add_union(start, end):
                return [start, end]




# DFS
class Solution:
    def findRedundantDirectedConnection(self, edges):
        N = len(edges)
        parent = {}
        candidates = []
        for u, v in edges:
            if v in parent:
                candidates.append((parent[v], v))
                candidates.append((u, v))
            else:
                parent[v] = u

        def orbit(node):
            seen = set()
            while node in parent and node not in seen:
                seen.add(node)
                node = parent[node]
            return node, seen

        root = orbit(1)[0]

        if not candidates:
            cycle = orbit(root)[1]
            for u, v in edges:
                if u in cycle and v in cycle:
                    ans = u, v
            return ans

        children = collections.defaultdict(list)
        for v in parent:
            children[parent[v]].append(v)

        seen = [True] + [False] * N
        stack = [root]
        while stack:
            node = stack.pop()
            if not seen[node]:
                seen[node] = True
                stack.extend(children[node])

        return candidates[all(seen)]