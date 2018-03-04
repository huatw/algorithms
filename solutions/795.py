class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        res, cnt, start = 0, 0, 0

        for i, n in enumerate(A):
            if R >= n:
                if n >= L:
                    cnt = i - start + 1
                res += cnt
            else:
                start = i + 1
                cnt = 0

        return res



