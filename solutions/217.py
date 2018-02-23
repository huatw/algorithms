class Solution:
    def containsDuplicate(self, nums):
        nset = set()

        for n in nums:
            if n in nset:
                return True
            nset.add(n)

        return False

class Solution:
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))
