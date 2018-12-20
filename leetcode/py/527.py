class Solution:
    def wordsAbbreviation(self, words):
        COUNT = True
        Trie = lambda: collections.defaultdict(Trie, {COUNT: 0})
        def build_trie(g_words):
            trie = Trie()
            for _, word in g_words:
                node = trie
                for ch in word[1:]:
                    node[COUNT] += 1
                    node = node[ch]
            return trie

        group_words_map = collections.defaultdict(list)
        for idx, word in enumerate(words):
            group_words_map[(len(word), word[0], word[-1])].append((idx, word))

        res = [None] * len(words)
        for g_words in group_words_map.values():
            trie = build_trie(g_words)

            for idx, word in g_words:
                node = trie
                for i, ch in enumerate(word[1:], 1):
                    if node[COUNT] == 1:
                        break
                    node = node[ch]
                if len(word) - 1 - i > 1:
                    res[idx] = word[:i] + str(len(word) - 1 - i) + word[-1]
                else:
                    res[idx] = word
        return res
