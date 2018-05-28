# DP O(mn)
class Solution(object):
    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)

        res = [[] for _ in range(len(s) + 1)]
        res[0].append('')

        for i in range(1, len(s) + 1):
            for j in range(i):
                if s[j:i] in wordSet and len(res[j]) > 0:
                    res[i].append((j, s[j:i]))

        def concatWords(idx):
            ret = []

            for preIdx, word in res[idx]:
                if preIdx == 0:
                    ret.append(word)
                else:
                    for preStr in concatWords(preIdx):
                        ret.append(preStr + ' ' + word)

            return ret

        return concatWords(-1)

