class Solution:
    def characterReplacement(self, s, k):
        lo = 0
        ch_cnt_map = collections.Counter()
        max_ch_cnt = 0
        res = 0

        for hi, ch in enumerate(s):
            ch_cnt_map[ch] += 1
            max_ch_cnt = max(max_ch_cnt, ch_cnt_map[ch])
            if hi - lo + 1 - max_ch_cnt > k:
                ch_cnt_map[s[lo]] -= 1
                lo += 1
            else:
                res = max(res, hi - lo + 1)

        return res
