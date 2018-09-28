class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ''

        res = strs[0]

        def calc_prefix(s1, s2):
            if len(s1) > len(s2):
                return calc_prefix(s2, s1)

            for i, (ch1, ch2) in enumerate(zip(s1, s2)):
                if ch1 != ch2:
                    return s1[:i]

            return s1

        for s in strs[1:]:
            res = calc_prefix(res, s)

        return res