class WordDistance:
    def __init__(self, words):
        self.cache = {}
        self.word_idx_map = collections.defaultdict(list)
        for i, word in enumerate(words):
            self.word_idx_map[word].append(i)

    def shortest(self, word1, word2):
        if word1 > word2:
            return self.shortest(word2, word1)

        if (word1, word2) not in self.cache:
            word1_lst, word2_lst = self.word_idx_map[word1], self.word_idx_map[word2]
            idx1, idx2 = 0, 0
            res = float('inf')

            while idx1 < len(word1_lst) and idx2 < len(word2_lst):
                res = min(res, abs(word1_lst[idx1] - word2_lst[idx2]))
                if word1_lst[idx1] < word2_lst[idx2]:
                    idx1 += 1
                else:
                    idx2 += 1

            self.cache[(word1, word2)] = res

        return self.cache[(word1, word2)]
