class Solution:
    def longestPalindrome(self, s):
        ch_cnt_map = collections.Counter(s)
        res = 0
        is_center_used = False

        for cnt in ch_cnt_map.values():
            even, odd = divmod(cnt, 2)
            res += even * 2
            if not is_center_used and odd:
                is_center_used = True
                res += 1

        return res