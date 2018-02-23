# important
# sliding window
class Solution:
    def minWindow(self, s, t):
        start, total, ret, map = 0, 0, '', collections.defaultdict(int)
        for ch in t:
            map[ch] += 1
            total += 1

        for i, ch in enumerate(s):
            if ch in map:
                map[ch] -= 1
                if map[ch] >= 0:
                    total -= 1
                while total == 0:
                    if not ret or i - start + 1 < len(ret):
                        ret = s[start: i+1]
                    if s[start] in map:
                        map[s[start]] += 1
                        if map[s[start]] > 0:
                            total += 1
                    start += 1

        return ret



