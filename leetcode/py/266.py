import collections
class Solution:
    def canPermutePalindrome(self, s):
        ch_cnt_map = collections.Counter(s)

        has_odd = False

        for (ch, cnt) in ch_cnt_map.items():
            if cnt % 2 != 0:
                if not has_odd:
                    has_odd = True
                else:
                    return False

        return True