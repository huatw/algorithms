class Solution:
    def minSubArrayLen(self, s, nums):
        start, sumN, res = 0, 0, len(nums)

        for i, n in enumerate(nums):
            sumN += n
            while sumN >= s:
                if i - start < res:
                    res = i - start
                sumN -= nums[start]
                start += 1

        return 0 if res == len(nums) else res + 1



