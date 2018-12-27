class Solution:
    def firstUniqChar(self, s):
        ch_cnt  = collections.Counter(s)
        for i, ch in enumerate(s):
            if ch_cnt[ch] == 1:
                return i
        return -1
