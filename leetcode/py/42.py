class Solution:
    def trap(self, heights):
        if not heights:
            return 0

        res = 0
        lo, hi = 0, len(heights) - 1
        left_bound, right_bound = heights[lo], heights[hi]

        while lo < hi:
            left_bound, right_bound = max(left_bound, heights[lo]), max(right_bound, heights[hi])
            if left_bound < right_bound:
                res += max(0, left_bound - heights[lo + 1])
                lo += 1
            else:
                res += max(0, right_bound - heights[hi - 1])
                hi -= 1

        return res

# thought:
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
#             ^   ^ ^ ^     ^
#           |   |       | |   |
# waters -> every water has left bound and right bound
class Solution:
    def trap(self, height):
        lo, hi = 0, len(height) - 1
        water = 0

        while lo < hi:
            if height[lo] < height[hi]:
                left_bound = height[lo]
                lo += 1
                while height[lo] < left_bound:
                    water += left_bound - height[lo]
                    lo += 1
            else:
                right_bound = height[hi]
                hi -= 1
                while height[hi] < right_bound:
                    water += right_bound - height[hi]
                    hi -= 1

        return water



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
