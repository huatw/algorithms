# O(n2) O(n2)
class Solution:
    def minCut(self, s):
        is_p = [[False] * len(s) for _ in range(len(s))]

        def expand(lo, hi):
            while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
                is_p[lo][hi] = True
                lo -= 1
                hi += 1

        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)

        min_cuts = []

        for i in range(len(s)):
            cuts = i
            for j in range(i + 1):
                if is_p[j][i]:
                    cuts = min(cuts, min_cuts[j - 1] + 1) if j != 0 else 0
            min_cuts.append(cuts)

        return min_cuts[-1]


# O(n2) O(n)
class Solution:
    def minCut(self, s):
        if not s:
            return 0

        lens = len(s)
        cuts = []
        isP = [[False] * i for i in range(1, lens + 1)]

        for i in range(lens):
            min_cut = i
            for j in range(i + 1):
                if (s[i] == s[j] and (i - j < 2 or isP[i - 1][j + 1])):
                    isP[i][j] = True
                    min_cut = 0 if j == 0 else min(min_cut, cuts[j - 1] + 1)
            cuts.append(min_cut)

        return cuts[-1]



