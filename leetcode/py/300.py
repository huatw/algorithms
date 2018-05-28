# IMPORTANT
#
# O n2
class Solution(object):
    def lengthOfLIS(self, nums):
        if not nums:
            return 0

        res = [0] * len(nums)
        maxLen = 0

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j] and res[i] <= res[j]:
                    res[i] = res[j] + 1
                    maxLen = max(maxLen, res[i])

        return maxLen + 1




# O nlogn
class Solution(object):
    def binarySearch(self, tails, n):
        start, end = 0, len(tails)-1

        while start < end:
            mid = (start + end) // 2
            if tails[mid] < n:
                start = mid + 1
            else:
                end = mid

        return start


    def lengthOfLIS(self, nums):
        if not nums:
            return 0

        # tail number of different length
        tails = [nums[0]]

        for n in nums:
            if n <= tails[0]:
                tails[0] = n
            elif n > tails[-1]:
                tails.append(n)
            else:
                pos = self.binarySearch(tails, n)
                tails[pos] = n

        return len(tails)







