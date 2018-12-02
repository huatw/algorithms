class Solution:
    def findLongestWord(self, s, d):
        def can_form_from(from_s, to_s):
            idx = 0
            for ch in to_s:
                while idx < len(from_s) and ch != from_s[idx]:
                    idx += 1
                if idx >= len(from_s):
                    return False
                idx += 1

            return True
        should_repace = lambda res, word: len(word) > len(res) or (len(word) == len(res) and word < res)
        res = ''
        for word in d:
            if len(word) <= len(s) and can_form_from(s, word) and should_repace(res, word):
                res = word

        return res