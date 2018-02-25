class Solution:
    def isSubsequence(self, s, t):
        if not s:
            return True

        idxS = 0

        for ch in t:
            if s[idxS] == ch:
                idxS += 1
                if idxS == len(s):
                    return True

        return False