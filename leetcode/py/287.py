# n midify array, negate array element with index number, duplicated number will negate element back
'''
Input: [1,3,4,2,2]
fast 1 2 2 ...
slow 1 3 2 4 2 4
'''
class Solution:
    def findDuplicate(self, nums):
        fast, slow = nums[0], nums[0]
        while True:
            fast, slow = nums[nums[fast]], nums[slow]
            if fast == slow:
                slow = nums[0]
                while fast != slow:
                    fast, slow = nums[fast], nums[slow]
                return fast



class Solution:
    def findDuplicate(self, nums):
        nums = sorted(nums)
        for prev_num, next_num in zip(nums, nums[1:]):
            if prev_num == next_num:
                return prev_num




class Solution:
    def findDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return nums
            seen.add(num)


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

