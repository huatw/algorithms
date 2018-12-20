class Solution:
    def longestCommonPrefix(self, strs):
        res = ''
        for chs in zip(*strs):
            if any(ch != chs[0] for ch in chs):
                break
            res += chs[0]

        return res
