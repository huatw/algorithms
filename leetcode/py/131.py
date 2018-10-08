'''
bba
b b a
bb a

abba
a bb a
a b b a

aabba     => [[s[:i]] + arr for i in range(1, len(s) + 1) for arr in self.partition(s[i:])]
1. a abba => [['a'] + arr for arr in partition('abba')]
a a bb a
a a b b a
2. aa bba => [['aa'] + arr for arr in partition('bba')]
aa b b a
aa bb a
3. aabb a => [['aabb'] + arr for arr in partition('a')]
'''

class Solution:
    def partition(self, s):
        if not s:
            return [[]]
        res = []
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:
                res += [[s[:i]] + arr for arr in self.partition(s[i:])]
        return res


# recursive + cache
class Solution:
    def partition(self, s):
        cache = {'': [[]]}

        def recur(start, end):
            if s[start:end] in cache:
                return cache[s[start:end]]
            res = []
            for i in range(start + 1, end + 1):
                if s[start:i] == s[start:i][::-1]:
                    res += [[s[start:i]] + arr for arr in recur(i, end)]
            cache[s[start:end]] = res
            return res

        return recur(0, len(s))


class Solution:
    def partition(self, s):
        ret = []

        for i in range(1, len(s) + 1):
            first = s[:i]
            if first == first[::-1]:
                arrs = self.partition(s[i:])
                if not arrs:
                    ret.append([first])
                else:
                    for arr in arrs:
                        ret.append([first] + arr)

        return ret