def permute(nums):
    def dfs(nums, path):
        if not nums:
            yield path
            return
        for i, num in enumerate(nums):
            if i != 0 and num == nums[i - 1]:
                continue
            yield from dfs(nums[:i] + nums[i + 1:], path + [num])
    yield from dfs(nums, [])

def is_valid(nums):
    one, two, three, four = nums
    return 24 > one * 10 + two >= 0 and 60 > three * 10 + four >= 0

class Solution:
    def largestTimeFromDigits(self, nums):
        nums = sorted(nums, reverse=True)
        for ret in permute(nums):
            if is_valid(ret):
                return str(ret[0]) + str(ret[1]) + ':' + str(ret[2]) + str(ret[3])
        return ''