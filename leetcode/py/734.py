class Solution:
    def areSentencesSimilar(self, words1, words2, pairs):
        if len(words1) != len(words2):
            return False

        synonym_map = collections.defaultdict(set)
        for word1, word2 in pairs:
            synonym_map[word1].add(word2)

        for (word1, word2) in zip(words1, words2):
            if word1 != word2 and word2 not in synonym_map[word1] and word1 not in synonym_map[word2]:
                return False
        return True
