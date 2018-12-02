class Solution:
    def findTheDifference(self, s, t):
        chs_cnt_map, cht_cnt_map = collections.Counter(s), collections.Counter(t)

        for ch, cnt in cht_cnt_map.items():
            if not (ch in chs_cnt_map and cnt == chs_cnt_map[ch]):
                return ch



class Solution:
    def findTheDifference(self, s, t):
        res = 0

        for c in s + t:
            res ^= ord(c)

        return chr(res)