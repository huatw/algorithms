# important
# sliding window
class Solution:
    def minWindow(self, s, t):
        lo = 0
        total = len(t)
        ch_map = collections.Counter(t)
        res = ''

        for hi, ch in enumerate(s):
            if ch not in ch_map:
                continue
            ch_map[ch] -= 1
            if ch_map[ch] >= 0:
                total -= 1

            while total == 0:
                if not res or hi - lo + 1 < len(res):
                    res = s[lo:hi + 1]
                if s[lo] in ch_map:
                    ch_map[s[lo]] += 1
                    if ch_map[s[lo]] > 0:
                        total += 1
                lo += 1

        return res
