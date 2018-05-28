class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()

        closet = math.inf

        for i in range(len(nums) - 2):
            start = i + 1
            end = len(nums) - 1

            while start < end:
                v = nums[i] + nums[start] + nums[end]

                if abs(closet - target) > abs(v - target):
                    closet = v

                if v == target:
                    return closet
                elif v < target:
                    start += 1
                else:
                    end -= 1

        return closet



