class Solution:
    def threeSum(self, nums):
        nums.sort()

        res = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            start, end = i + 1, len(nums) - 1
            while start < end:
                v = nums[start] + nums[end] + nums[i]
                if v == 0:
                    res.append([nums[start], nums[end], nums[i]])
                    start += 1
                    end -= 1
                    while start < end and nums[start - 1] == nums[start]:
                        start += 1
                    while start < end and nums[end + 1] == nums[end]:
                        end -= 1
                elif v < 0:
                    start += 1
                else:
                    end -= 1

        return res



class Solution:
    def threeSum(self, nums):
        nums.sort()

        res = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            start, end = i + 1, len(nums) - 1
            while start < end:
                v = nums[start] + nums[end] + nums[i]
                if v == 0:
                    res.append((nums[start], nums[end], nums[i]))
                    start += 1
                    end -= 1
                elif v < 0:
                    start += 1
                else:
                    end -= 1

        return [*map(list, set(res))]



