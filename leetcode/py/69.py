class Solution:
    def mySqrt(self, x):
        lo, hi = 0, x
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if (mid + 1) ** 2 > x:
                hi = mid
            else:
                lo = mid + 1
        return lo
