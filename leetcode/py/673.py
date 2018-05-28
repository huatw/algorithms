# On2
class Solution:
    def findNumberOfLIS(self, nums):
        if not nums:
            return 0

        lens, cnts = [1] * len(nums), [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if lens[i] == lens[j] + 1:
                        cnts[i] += cnts[j]
                    elif lens[i] < lens[j] + 1:
                        cnts[i] = cnts[j]
                        lens[i] = lens[j] + 1

        max_len = max(lens)
        return sum(cnt for l, cnt in zip(lens, cnts) if l == max_len)


