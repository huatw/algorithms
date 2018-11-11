class Solution:
    def shortestWordDistance(self, words, word1, word2):
        if word1 == word2:
            idx = -float('inf')
            res = float('inf')
            for i, word in enumerate(words):
                if word == word1:
                    res = min(res, i - idx)
                    idx = i
            return res

        idx1, idx2 = -float('inf'), -float('inf')
        res = float('inf')

        for i, word in enumerate(words):
            if word == word1:
                res = min(res, i - idx2)
                idx1 = i
            elif word == word2:
                res = min(res, i - idx1)
                idx2 = i

        return res