# DP MLE!!!!
class Solution:
    def wordBreak(self, s, word_dict):
        word_set = set(word_dict)
        res = [[] for _ in range(len(s) + 1)]
        res[0].append('')

        for i in range(1, len(s) + 1):
            for j in range(i):
                if s[j:i] in word_set and len(res[j]) > 0:
                    if i == len(s):
                        for pre_str in res[j]:
                            res[i].append(pre_str + s[j:i])
                    else:
                        for pre_str in res[j]:
                            res[i].append(pre_str + s[j:i] + ' ')

        return res[-1]


# DP
class Solution:
    def wordBreak(self, s, word_dict):
        word_set = set(word_dict)
        res = [[] for _ in range(len(s) + 1)]
        res[0].append('')

        for i in range(1, len(s) + 1):
            for j in range(i):
                if s[j:i] in word_set and len(res[j]) > 0:
                    res[i].append((j, s[j:i]))

        def concat_words(idx):
            ret = []
            for pre_idx, word in res[idx]:
                if pre_idx == 0:
                    ret.append(word)
                else:
                    for pre_str in concat_words(pre_idx):
                        ret.append(pre_str + ' ' + word)
            return ret

        return concat_words(-1)
