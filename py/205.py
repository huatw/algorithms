# two map
class Solution:
    def isIsomorphic(self, s, t):
        t2s, s2t = {}, {}

        if len(s) != len(t):
            return False

        for chs, cht in zip(s, t):
            if chs not in s2t and cht not in t2s:
                s2t[chs] = cht
                t2s[cht] = chs
            elif cht not in t2s or chs not in s2t or t2s[cht] != chs or s2t[chs] != cht:
                return False

        return True




class Solution:
    def isIsomorphic(self, s, t):
        return [*map(s.find, s)] == [*map(t.find, t)]




def wordPattern(self, pattern, str):
    # set ch in s with minimal ch index
    f = lambda s: [*map({}.setdefault, s, range(len(s)))]
    return f(pattern) == f(str.split())




def wordPattern(self, pattern, str):
    s = pattern
    t = str.split()

    return len(set(zip(s, t))) == len(set(s)) == len(set(t)) and len(s) == len(t)



