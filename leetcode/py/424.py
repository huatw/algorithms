class Solution:
    def characterReplacement(self, s, k):
        ch_cnt_map = collections.defaultdict(int)
        max_ch_cnt = 0
        total = 0
        lo = 0
        res = 0

        for hi, ch in enumerate(s):
            total += 1
            ch_cnt_map[ch] += 1
            max_ch_cnt = max(max_ch_cnt, ch_cnt_map[ch])
            if total - max_ch_cnt > k:
                total -= 1
                ch_cnt_map[s[lo]] -= 1
                lo += 1
            else:
                res = max(res, hi - lo)

        return res