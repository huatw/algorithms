class UnionFind:
    def __init__(self):
        self.m = {}

    def union(self, w1, w2):
        if w1 not in self.m:
            self.m[w1] = w1
        if w2 not in self.m:
            self.m[w2] = w2
        r1, r2 = self.find(w1), self.find(w2)
        if r1 != r2:
            self.m[r1] = r2

    def find(self, w):
        if self.m[w] != w:
            self.m[w] = self.find(self.m[w])
        return self.m[w]

    def is_similar(self, w1, w2):
        return w1 == w2 or (w1 in self.m and w2 in self.m and self.find(w1) == self.find(w2))

class Solution:
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        if len(words1) != len(words2):
            return False

        uf = UnionFind()
        for w1, w2 in pairs:
            uf.union(w1, w2)

        return all(uf.is_similar(w1, w2) for w1, w2 in zip(words1, words2))