class Solution(object):
    def circularArrayLoop(self, nums):
        if not nums or len(nums) < 2:
            return False

        N = len(nums)
        for i in range(N):
            if type(nums[i]) != int:
                continue
            if nums[i] % N == 0:
                continue

            direction = nums[i] > 0

            mark = str(i)
            while type(nums[i]) == int and direction ^ (nums[i] < 0) and nums[i] % N != 0:
                nums[i], i = mark, (i + nums[i]) % N

            if nums[i] == mark:
                return True

        return False