# binary
class Solution:
    def search(self, nums, target):
        if not nums:
            return False

        lo, hi = 0, len(nums) - 1

        while lo < hi:
            mid = lo + (hi - lo) // 2

            if nums[mid] == target:
                return True

            if nums[lo] == nums[hi] and nums[lo] == nums[mid]:
                lo += 1
                hi -= 1
            else:
                if nums[mid] < target <= nums[hi] or (nums[mid] > nums[hi] and (target > nums[mid] or target <= nums[hi])):
                    lo = mid + 1
                else:
                    hi = mid - 1

        return nums[lo] == target
