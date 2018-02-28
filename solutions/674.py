class Solution(object):
    def findLengthOfLCIS(self, nums):
        if not nums:
            return 0

        cnt, maxCnt = 1, 0

        for i, n in enumerate(nums[1:]):
            if n > nums[i]:
                cnt += 1
            else:
                cnt, maxCnt = 1, max(maxCnt, cnt)

        return max(maxCnt, cnt)



