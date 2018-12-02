class UnionFind:
    def __init__(self):
        self.m = {}
    def add_union(self, word1, word2):
        if word1 in self.m and word2 in self.m:
            self.union(word1, word2)
        elif word1 in self.m:
            self.m[word2] = word1
        elif word2 in self.m:
            self.m[word1] = word2
        else:
            self.m[word1] = word2
            self.m[word2] = word2
    def union(self, word1, word2):
        r1, r2 = self.find(word1), self.find(word2)
        if r1 != r2:
            self.m[r1] = r2
    def find(self, word):
        if self.m[word] != word:
            self.m[word] = self.find(self.m[word])
        return self.m[word]
    def is_synonym(self, word1, word2):
        return word1 in self.m and word2 in self.m and self.find(word1) == self.find(word2)


class Solution:
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        if len(words1) != len(words2):
            return False
        uf = UnionFind()
        for (word1, word2) in pairs:
            uf.add_union(word1, word2)

        for (word1, word2) in zip(words1, words2):
            if word1 != word2 and not uf.is_synonym(word1, word2):
                return False
        return True
