# two pointer + map
class Solution:
    def findAnagrams(self, s, p):
        s_dict = collections.defaultdict(int)
        lo = 0
        res = []

        for ch in p:
            s_dict[ch] += 1

        for hi, ch in enumerate(s):
            s_dict[ch] -= 1
            while s_dict[ch] < 0:
                s_dict[s[lo]] += 1
                lo += 1
            if hi - lo == len(p) - 1:
                res.append(lo)

        return res
