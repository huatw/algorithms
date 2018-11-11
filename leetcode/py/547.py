class UnionFind:
    def __init__(self, size):
        self.people = [i for i in range(size)]
        self.size = size

    def union(self, p1, p2):
        root1, root2 = self.find(p1), self.find(p2)
        if root1 == root2:
            return
        self.size -= 1
        self.people[root1] = root2

    def find(self, p):
        if p == self.people[p]: # parent is itself
            return p
        self.people[p] = self.find(self.people[p])
        return self.people[p]

class Solution:
    def findCircleNum(self, M):
        size = len(M)
        uf = UnionFind(size)

        for i in range(size):
            for j in range(size):
                if M[i][j] == 1:
                    uf.union(i, j)

        return uf.size



class Solution:
    def findCircleNum(self, M):
        circle_map = collections.defaultdict(list)

        for i, row in enumerate(M):
            for j, relation in enumerate(row):
                if relation == 1:
                    circle_map[i].append(j)

        res = 0
        seen_set = set()

        for k, arr in circle_map.items():
            if k not in seen_set:
                seen_set.add(k)
                res += 1
                stack = arr
                for friend in stack:
                    if friend not in seen_set:
                        seen_set.add(friend)
                        stack += circle_map[friend]

        return res

