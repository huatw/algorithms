class Solution:
    def mySqrt(self, x):
        if x == 0:
            return 0

        lo, hi = 1, x

        while lo < hi:
            mid = lo + (hi - lo) // 2

            if mid * mid > hi:
                hi = mid - 1
            else:
                lo = mid + 1

        return lo