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



