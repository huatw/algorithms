# binary
class Solution:
    def search(self, nums, target):
        if not nums:
            return -1

        lo, hi = 0, len(nums) - 1

        while lo < hi:
            mid = lo + (hi - lo) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] < target <= nums[hi] or (nums[mid] > nums[hi] and (target > nums[mid] or target <= nums[hi])):
                lo = mid + 1
            else:
                hi = mid - 1

        return lo if nums[lo] == target else -1
