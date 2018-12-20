# errr... based on previous solutions
class Solution:
    def generateAbbreviations(self, word):
        def dfs(idx, acc, cnt):
            if len(word) == idx:
                return [acc + (str(cnt) if cnt > 0 else '')]
            return dfs(idx + 1, acc, cnt + 1) + dfs(idx + 1, acc + (str(cnt) if cnt > 0 else '') + word[idx], 0)

        return dfs(0, '', 0)

    def validWordAbbreviation(self, word, abbr):
        idx_w, idx_a = 0, 0
        while idx_w < len(word) and idx_a < len(abbr):
            if abbr[idx_a] == '0':
                return False
            if abbr[idx_a].isdigit():
                digit = ''
                while idx_a < len(abbr) and abbr[idx_a].isdigit():
                    digit += abbr[idx_a]
                    idx_a += 1
                idx_w += int(digit)
            else:
                if abbr[idx_a] != word[idx_w]:
                    return False
                idx_a += 1
                idx_w += 1

        return idx_w == len(word) and idx_a == len(abbr)

    def minAbbreviation(self, target, dictionary):
        words = [word for word in dictionary if len(word) == len(target)]
        if not words:
            return str(len(target))

        for abbr in sorted(self.generateAbbreviations(target), key=lambda w: len(w)):
            if all(not self.validWordAbbreviation(word, abbr) for word in words):
                return abbr
