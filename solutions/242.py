class Solution:
    def isAnagram(self, s, t):
        map = collections.defaultdict(int)
        for ch in s:
            map[ch] += 1

        for ch in t:
            map[ch] -= 1

        for v in map.values():
            if v != 0:
                return False

        return True

class Solution:
    def isAnagram(self, s, t):
        map1 = collections.defaultdict(int)
        map2 = collections.defaultdict(int)
        for ch in s:
            map1[ch] += 1

        for ch in t:
            map2[ch] += 1

        return map1 == map2
