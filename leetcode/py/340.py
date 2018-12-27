class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        total = 0
        ch_cnt_map = collections.Counter()
        lo = 0
        res = 0

        for hi, ch in enumerate(s):
            if ch_cnt_map[ch] == 0:
                total += 1
            ch_cnt_map[ch] += 1
            while total > k:
                ch_cnt_map[s[lo]] -= 1
                if ch_cnt_map[s[lo]] == 0:
                    total -= 1
                lo += 1
            res = max(res, hi - lo + 1)

        return res
