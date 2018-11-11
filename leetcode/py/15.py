class Solution:
    def threeSum(self, nums):
        nums = sorted(nums)
        res = []

        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                total = nums[i] + nums[lo] + nums[hi]
                if total < 0:
                    lo += 1
                elif total > 0:
                    hi -= 1
                else:
                    res.append([nums[i], nums[lo], nums[hi]])
                    lo += 1
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1
                    hi -= 1
                    while lo < hi and nums[hi] == nums[hi + 1]:
                        hi -= 1

        return res



class Solution:
    def threeSum(self, nums):
        nums.sort()

        res = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            start, end = i + 1, len(nums) - 1
            while start < end:
                v = nums[start] + nums[end] + nums[i]
                if v == 0:
                    res.append([nums[start], nums[end], nums[i]])
                    start += 1
                    end -= 1
                    while start < end and nums[start - 1] == nums[start]:
                        start += 1
                    while start < end and nums[end + 1] == nums[end]:
                        end -= 1
                elif v < 0:
                    start += 1
                else:
                    end -= 1

        return res
