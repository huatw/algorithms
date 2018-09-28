class Solution:
    def longestPalindrome(self, s):
        res = ''

        def helper(lo, hi):
            nonlocal res
            while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
                lo -= 1
                hi += 1
            str_len = hi - lo - 1
            if str_len > len(res):
                res = s[lo + 1:hi]

        for i in range(len(s)):
            helper(i, i)
            helper(i, i + 1)

        return res
