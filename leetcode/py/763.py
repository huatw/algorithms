# two pointer greedy
class Solution:
    def partitionLabels(self, S):
        res = []
        idx_map = {ch: i for i, ch in enumerate(S)}
        lo, hi = -1, idx_map[S[0]]

        for i, ch in enumerate(S):
            if i < hi:
                hi = max(hi, idx_map[ch])
            else:
                res.append(hi - lo)
                if i != len(S) - 1:
                    lo, hi = hi, idx_map[S[i + 1]]

        return res
