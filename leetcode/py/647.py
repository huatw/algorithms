# On2
class Solution:
    def countSubstrings(self, s):
        res = 0

        def find(lo, hi):
            nonlocal res
            while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
                res += 1
                lo -= 1
                hi += 1

        for i, center in enumerate(s):
            # find from i and i + 1
            find(i, i + 1)
            # find from i
            find(i, i)

        return res

# ?
def countSubstrings(self, S):
    def manachers(S):
        A = '@#' + '#'.join(S) + '#$'
        Z = [0] * len(A)
        center = right = 0
        for i in xrange(1, len(A) - 1):
            if i < right:
                Z[i] = min(right - i, Z[2 * center - i])
            while A[i + Z[i] + 1] == A[i - Z[i] - 1]:
                Z[i] += 1
            if i + Z[i] > right:
                center, right = i, i + Z[i]
        return Z

    return sum((v+1)/2 for v in manachers(S))