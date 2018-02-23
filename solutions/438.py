class Solution:
    def findAnagrams(self, s, p):
        start, res = 0, []
        map = collections.defaultdict(int)

        for ch in p:
            map[ch] += 1

        for i, ch in enumerate(s):
            if ch in map:
                map[ch] -= 1
                while map[ch] < 0:
                    map[s[start]] += 1
                    start += 1
                if map[ch] == 0 and i - start == len(p) - 1:
                    res.append(start)
            else:
                while start <= i:
                    if s[start] in map:
                        map[s[start]] += 1
                    start += 1

        return res