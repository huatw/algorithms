# this question is important

# priority q
class Solution:
    def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums)[k-1]


class Solution:
    def findKthLargest(self, nums, k):
        hq = []
        for num in nums:
            if len(hq) == k:
                heapq.heappushpop(hq, num)
            else:
                heapq.heappush(hq, num)

        return hq[0]



# quick selection O(n)?
class Solution:
    def findKthLargest(self, nums, k):
        if k > len(nums):
            return
        k = len(nums) - k + 1
        lo, hi = 0, len(nums) - 1
        while True:
            idx = self.partition(lo, hi, nums)
            if idx + 1 > k:
                hi = idx - 1
            elif idx + 1 < k:
                lo = idx + 1
            else:
                return nums[idx]

    def partition(self, lo, hi, nums): # bisect right
        target= nums[hi]
        last = hi
        hi = hi - 1
        while lo <= hi:
            if nums[lo] <= target:
                lo += 1
            elif nums[hi] > target:
                hi -= 1
            else:
                nums[lo], nums[hi] = nums[hi], nums[lo]
                lo += 1
                hi -= 1
        nums[lo], nums[last] = nums[last], nums[lo]
        return lo
