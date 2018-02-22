# this question is important

# priority q
class Solution:
    def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums)[k-1]




# quick selection O(n)?
class Solution:
    def findKthLargest(self, nums, k):
        if not nums:
            return 0

        left, right = 0, len(nums)-1

        while True:
            pos = self.partition(nums, left, right)
            if pos + 1 == k:
                return nums[pos]
            elif pos + 1 > k:
                right = pos - 1
            else:
                left = pos + 1


    def partition(self, nums, left, right):
        pivot = nums[left]
        l, r = left + 1, right

        while l <= r:
            if (nums[l] < pivot and nums[r] > pivot):
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            if nums[l] >= pivot:
                l += 1
            if nums[r] <= pivot:
                r -= 1

        nums[left], nums[r] = nums[r], nums[left]
        return r


