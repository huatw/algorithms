class Solution:
    def findContentChildren(self, g, s):
        if not g or not s:
            return 0

        g.sort()
        s.sort()

        idx = 0
        for cookie in s:
            if g[idx] <= cookie:
                idx += 1
                if idx == len(g):
                    return idx

        return idx



