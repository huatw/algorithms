class Solution:
    def maxSubArray(self, nums):
        max_subarr_ends = [-float('inf')]
        max_subarr_at = [-float('inf')]

        for num in nums:
            max_subarr_at.append(max(num, max_subarr_at[-1], num + max_subarr_ends[-1]))
            max_subarr_ends.append(max(num, num + max_subarr_ends[-1]))

        return max_subarr_at[-1]


class Solution:
    def maxSubArray(self, nums):
        max_subarr_ends = -float('inf')
        max_subarr_at = -float('inf')

        for num in nums:
            max_subarr_at.append(max(num, max_subarr_at, num + max_subarr_ends))
            max_subarr_ends.append(max(num, num + max_subarr_ends))

        return max_subarr_at






# space o(n)
class Solution:
    def maxSubArray(self, nums):
        res = [-float('inf')]

        for n in nums:
            res.append(max(n, res[-1] + n))

        return max(res)


# space o(1)
class Solution:
    def maxSubArray(self, nums):
        res, prev_max = -float('inf'), -float('inf')

        for n in nums:
            prev_max = max(n, prev_max + n)
            res = max(prev_max, res)

        return res


class Solution(object):
    def maxSubArray(self, nums):
        if not nums:
            return 0

        res, val = nums[0], nums[0]

        for n in nums[1:]:
            if val < 0:
                val = n
            else:
                val += n
            res = max(res, val)

        return res



