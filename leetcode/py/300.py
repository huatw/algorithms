# IMPORTANT
# O n2
class Solution:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        res = []

        for num in nums:
            res.append(1)
            for i in range(len(res) - 1):
                if nums[i] < num and res[i] >= res[-1]:
                    res[-1] = res[i] + 1

        return max(res)


# O nlogn
class Solution:
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


class Solution:
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
                pos = bisect.bisect_left(tails, n)
                tails[pos] = n

        return len(tails)
