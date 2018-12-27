class UnionFind:
    def __init__(self):
        self.m = {}

    def union(self, n1, n2):
        if n1 not in self.m:
            self.m[n1] = n1
        if n2 not in self.m:
            self.m[n2] = n2
        r1, r2 = self.find(n1), self.find(n2)
        if r1 != r2:
            self.m[r1] = r2
            return True
        return False

    def find(self, n):
        if self.m[n] != n:
            self.m[n] = self.find(self.m[n])
        return self.m[n]

class Solution:
    def findRedundantDirectedConnection(self, edges):
        def has_cycle(start, end, end_start_map):
            while start in end_start_map:
                start = end_start_map[start]
                if end == start:
                    return True
            return False

        candidates = []
        end_starts_map = {}
        for start, end in edges:
            if end in end_starts_map:
                candidates = [(end_starts_map[end], end), (start, end)]
            else:
                end_starts_map[end] = start

        if candidates:
            return candidates[0] if has_cycle(*candidates[0], end_starts_map) else candidates[1]

        uf = UnionFind()
        for edge in edges:
            if not uf.union(*edge):
                return edge



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