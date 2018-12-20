class Solution:
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
