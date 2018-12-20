class Solution:
    def generateAbbreviations(self, word):
        def dfs(idx, acc, cnt):
            if len(word) == idx:
                return [acc + (str(cnt) if cnt > 0 else '')]
            return dfs(idx + 1, acc, cnt + 1) + dfs(idx + 1, acc + (str(cnt) if cnt > 0 else '') + word[idx], 0)

        return dfs(0, '', 0)


class Solution:
    def generateAbbreviations(self, word):
        def dfs(idx, acc, cnt):
            if len(word) == idx:
                res.append(acc + (str(cnt) if cnt > 0 else ''))
                return
            dfs(idx + 1, acc, cnt + 1)
            dfs(idx + 1, acc + (str(cnt) if cnt > 0 else '') + word[idx], 0)

        res = []
        dfs(0, '', 0)
        return res


# bad
class Solution:
    def generateAbbreviations(self, word):
        res = []

        def combine(chs):
            res = []
            for ch in chs:
                if res and isinstance(ch, int) and isinstance(res[-1], int):
                    res[-1] += ch
                else:
                    res.append(ch)
            return tuple(res)

        level = [tuple(word)]
        while level:
            next_level = []
            for chs in level:
                res.append(''.join(str(ch) for ch in chs))
                for i, ch in enumerate(chs):
                    if isinstance(ch, str):
                        next_level.append(chs[:i] + (1,) + chs[i + 1:])
            level = set(combine(chs) for chs in next_level)

        return res