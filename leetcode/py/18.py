# k-sum
def k_sum(nums, target, k):
    N = len(nums)
    nums = sorted(nums)
    res = []

    def recur(lo, hi, acc):
        if hi < N - 1:
            for i in range(lo, hi):
                if i > lo and nums[i] == nums[i - 1]:
                    continue
                acc.append(nums[i])
                recur(i + 1, hi + 1, acc)
                acc.pop()
            return

        while lo < hi:
            total = sum(acc) + nums[lo] + nums[hi]
            if total < target:
                lo += 1
            elif total > target:
                hi -= 1
            else:
                res.append((*acc, nums[lo], nums[hi]))
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1
                while lo < hi and nums[hi] == nums[hi + 1]:
                    hi -= 1

    recur(0, N - k + 1, [])
    return res

class Solution:
    def fourSum(self, nums, target):
        return k_sum(nums, target, 4)




class Solution:
    def fourSum(self, nums, target):
        nums = sorted(nums)
        res = []

        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                lo, hi = j + 1, len(nums) - 1
                while lo < hi:
                    total = nums[i] + nums[j] + nums[lo] + nums[hi]
                    if total < target:
                        lo += 1
                    elif total > target:
                        hi -= 1
                    else:
                        res.append((nums[i], nums[j], nums[lo], nums[hi]))
                        lo += 1
                        hi -= 1
                        while lo < hi and nums[lo] == nums[lo - 1]:
                            lo += 1
                        while lo < hi and nums[hi] == nums[hi + 1]:
                            hi -= 1

        return res
