class Solution:
    def diStringMatch(self, S):
        if not S:
            return []

        res = []
        lo, hi = 0, len(S)

        for direction in S:
            if direction == 'I':
                res.append(lo)
                lo += 1
            elif direction == 'D':
                res.append(hi)
                hi -= 1

        return res + [lo]