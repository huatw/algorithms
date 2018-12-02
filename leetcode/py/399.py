'''
equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]
'''
# DFS
class Solution:
    def calcEquation(self, equations, values, queries):
        from_to_map = collections.defaultdict(collections.defaultdict)

        for ((f, t), val) in zip(equations, values):
            from_to_map[f][t] = val
            from_to_map[t][f] = 1.0 / val

        def query_val(f, t, seen):
            if f == t:
                return 1.0
            for (k, v) in from_to_map[f].items():
                if k not in seen:
                    seen.add(k)
                    ret = query_val(k, t, seen)
                    if ret != None:
                        return v * ret
                    seen.pop(k)
            return

        res = [query_val(f, t, set()) if f in from_to_map else None for (f, t) in queries]
        return [v if v != None else -1.0 for v in res]



# Union Find
class UnionFind:
    def __init__(self):
        self.from_to_map = {}
    def add_union(self, f, t, val):
        if f in self.from_to_map or t in self.from_to_map:
            self.union(f, t, val)
        else:
            self.add(f, t, val)
    def add(self, f, t, val):
        self.from_to_map[f] = (t, val)
        self.from_to_map[t] = (t, 1.0)
    def union(self, f, t, val):
        if f in self.from_to_map and t in self.from_to_map:# union two graph
            root_f, val_f = self.find(f)
            root_t, val_t = self.find(t)
            self.from_to_map[root_f] = (root_t, val * val_t / val_f)
        elif f in self.from_to_map:
            self.from_to_map[t] = (f, 1.0 / val)
        elif t in self.from_to_map:
            self.from_to_map[f] = (t, val)
    def find(self, node):
        p_node, val = self.from_to_map[node]
        if p_node != node:
            r_node, total = self.find(p_node)
            self.from_to_map[node] = (r_node, total * val)
        return self.from_to_map[node]
    def search(self, f, t):
        if f not in self.from_to_map or t not in self.from_to_map:
            return -1.0
        root_f, val_f = self.find(f)
        root_t, val_t = self.find(t)
        if root_f != root_t:
            return -1.0
        return val_f / val_t

class Solution:
    def calcEquation(self, equations, values, queries):
        uf = UnionFind()
        for ((f, t), val) in zip(equations, values):
            uf.add_union(f, t, val)

        return [uf.search(f, t) for (f, t) in queries]
