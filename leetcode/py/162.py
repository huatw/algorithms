'''
12321
'''
class Solution:
    def findPeakElement(self, nums):
        def search(start, end):
            if start == end:
                return start
            mid = (start + end) // 2
            if nums[mid] > nums[mid + 1]:
                return search(start, mid)
            return search(mid + 1, end)

        return search(0, len(nums) - 1)


class Solution:
    def findPeakElement(self, nums):
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1

        return left
