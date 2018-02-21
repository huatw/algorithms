class Solution:
    def removeDuplicates(self, nums):
        idx, prevN, pprevN = 0, None, None

        for i, n in enumerate(nums):
            if not (n == prevN and n == pprevN):
                if i != idx:
                    nums[idx] = n
                idx += 1
            prevN, pprevN = n, prevN

        return idx




class Solution(object):
    def removeDuplicates(self, nums):
        tail = 0
        for num in nums:
            if tail < 2 or num != nums[tail - 1] or num != nums[tail - 2]:
                nums[tail] = num
                tail += 1
        return tail


