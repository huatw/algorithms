class Solution:
    def areSentencesSimilar(self, words1, words2, pairs):
        if len(words1) != len(words2):
            return False

        word_map = collections.defaultdict(set)
        for w1, w2 in pairs:
            word_map[w1].add(w2)

        def is_same(w1, w2):
            return w1 == w2 or w2 in word_map[w1] or w1 in word_map[w2]

        return all(is_same(w1, w2) for w1, w2 in zip(words1, words2))

