class Solution:
    def titleToNumber(self, s):
        res = 0
        for ch in s:
            res = res * 26 + (ord(ch) - ord('A') + 1)
        return res