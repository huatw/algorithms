# two pointer

class Solution:
    def trap(self, height):
        lo, hi = 0, len(height) - 1
        lo_max, hi_max = 0, 0
        res = 0

        while lo < hi:
            # move lo
            if height[lo] < height[hi]:
                if height[lo] >= lo_max:
                    lo_max = height[lo]
                else:
                    res += lo_max - height[lo]
                lo += 1
            # move hi
            else:
                if height[hi] >= hi_max:
                    hi_max = height[hi]
                else:
                    res += hi_max - height[hi]
                hi -= 1

        return res
