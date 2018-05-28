# two map
class Solution:
    def wordPattern(self, pattern, str):
        p2s, s2p, arr = {}, {}, str.split(' ')

        if len(arr) != len(pattern):
            return False

        for p, s in zip(pattern, arr):
            if p not in p2s and s not in s2p:
                p2s[p] = s
                s2p[s] = p
            elif p not in p2s or s not in s2p or p2s[p] != s or s2p[s] != p:
                return False

        return True




def wordPattern(self, pattern, d str):
    s = pattern
    t = str.split()

    return map(s.find, s) == map(t.index, t)




def wordPattern(self, pattern, str):
    # set ch in s with minimal ch index
    f = lambda s: map({}.setdefault, s, range(len(s)))

    return f(pattern) == f(str.split())




def wordPattern(self, pattern, str):
    s = pattern
    t = str.split()

    return len(set(zip(s, t))) == len(set(s)) == len(set(t)) and len(s) == len(t)



