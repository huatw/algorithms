# more general approach
class Solution:
    def find_rotate_point(self, nums):
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] > nums[mid + 1]:
                return mid
            if nums[mid] > nums[-1]:
                lo = mid + 1
            else:
                hi = mid - 1

    def binary_search(self, nums, st, ed, target):
        lo, hi = st, ed
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] > target:
                hi = mid - 1
            elif nums[mid] < target:
                lo = mid + 1
            else:
                return mid
        return lo if nums[lo] == target else -1

    def search(self, nums, target):
        if not nums:
            return -1

        idx = self.find_rotate_point(nums)
        ret = self.binary_search(nums, 0, idx, target)
        if ret == -1:
            return self.binary_search(nums, idx + 1, len(nums) - 1, target)
        return ret


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
