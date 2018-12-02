# O(n) O(1)
class Solution:
    def majorityElement(self, nums):
        res = None
        cnt = 0

        for num in nums:
            if cnt == 0:
                res = num
            cnt += 1 if res == num else -1

        return res



# O(n) O(n)
class Solution:
    def majorityElement(self, nums):
        n_map = collections.defaultdict(int)

        for n in nums:
            n_map[n] += 1
            if n_map[n] > len(nums) / 2:
                return n




# O(nlogn) O(1)
class Solution:
    def majorityElement(self, nums):
        nums = sorted(nums)
        cnt = 0
        res = None
        for num in nums:
            if res != num:
                res = num
                cnt = 0
            cnt += 1
            if cnt > len(nums) / 2:
                return res
