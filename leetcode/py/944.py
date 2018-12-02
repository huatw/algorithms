class Solution:
    def minDeletionSize(self, A):
        res = 0

        for col in zip(*A):
            for pre_ch, next_ch in zip(col, col[1:]):
                if pre_ch > next_ch:
                    res += 1
                    break

        return res


class Solution:
    def minDeletionSize(self, A):
        res = 0

        for col in zip(*A):
            if any(pre_ch > next_ch for pre_ch, next_ch in zip(col, col[1:])):
                res += 1

        return res