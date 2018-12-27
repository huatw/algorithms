class Solution:
    def findAnagrams(self, s, p):
        ch_cnt_map = collections.Counter(p)

        res = []
        lo = 0
        for hi, ch in enumerate(s):
            ch_cnt_map[ch] -= 1
            while ch_cnt_map[ch] < 0:
                ch_cnt_map[s[lo]] += 1
                lo += 1
            if hi - lo + 1 == len(p):
                res.append(lo)
        return res
