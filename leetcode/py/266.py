class Solution:
    def canPermutePalindrome(self, s):
        ch_cnt_map = collections.Counter(s)
        has_odd = False
        for cnt in ch_cnt_map.values():
            if cnt % 2 != 0:
                if has_odd:
                    return False
                has_odd = True
        return True

