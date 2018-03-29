class Solution:
    def fourSum(self, nums, target):
        nums.sort()

        res = []

        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue

                start, end = j + 1, len(nums) - 1

                while start < end:
                    v = nums[i] + nums[j] + nums[start] + nums[end]

                    if v == target:
                        res.append([nums[i], nums[j], nums[start], nums[end]])
                        start += 1
                        end -= 1
                        while start < end and nums[start] == nums[start-1]:
                            start += 1
                        while start < end and nums[end] == nums[end+1]:
                            end -= 1
                    elif v < target:
                        start += 1
                    else:
                        end -= 1

        return res



