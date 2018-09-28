# n midify array, negate array element with index number, duplicated number will negate element back

# n logn
class Solution:
    def findDuplicate(self, nums):
        lo, hi = 1, len(nums) - 1

        while lo < hi:
            mid = lo + (hi - lo) // 2
            cnt = 0

            for num in nums:
                if hi >= num > mid:
                    cnt += 1

            if cnt > hi - mid:
                lo = mid + 1
            else:
                hi = mid

        return lo

