class Solution(object):
    def canPartition(self, nums):
        total = sum(nums)

        if total % 2 != 0:
            return False

        # nums.sort()
        s = set([0])

        for n in nums:
            ss = set()
            for res in s:
                newRes = n + res
                if newRes == total / 2:
                    return True
                ss.add(newRes)
            s |= ss

        return False




class Solution(object):
    def canPartition(self, nums):
        total = sum(nums)

        if total % 2 == 0:
            s = set([0])

            for n in nums:
                s |= {n + res for res in s}
                if total / 2 in s:
                    return True

        return False

