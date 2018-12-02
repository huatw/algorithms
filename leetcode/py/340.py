'''
Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.

Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.
'''
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        res = 0
        lo = 0
        ch_cnt = 0
        ch_cnt_map = collections.defaultdict(int)

        for hi, ch in enumerate(s):
            if ch_cnt_map[ch] == 0:
                ch_cnt += 1
            ch_cnt_map[ch] += 1

            while ch_cnt > k:
                ch_cnt_map[s[lo]] -= 1
                if ch_cnt_map[s[lo]] == 0:
                    ch_cnt -= 1
                lo += 1

            res = max(res, hi - lo + 1)

        return res