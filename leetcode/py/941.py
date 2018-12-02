class Solution:
    def validMountainArray(self, nums):
        if len(nums) < 3:
            return False

        i = 1
        while i < len(nums) and nums[i] > nums[i - 1]:
            i += 1

        if i == 1 or i == len(nums):
            return False

        while i < len(nums) and nums[i] < nums[i - 1]:
            i += 1

        return i == len(nums)



class Solution:
    def validMountainArray(self, A):
        if len(A) < 3:
            return False

        is_inc = True

        for i, (prev_n, next_n) in enumerate(zip(A, A[1:])):
            if prev_n == next_n:
                return False
            if is_inc:
                if prev_n > next_n:
                    if i == 0:
                        return False
                    is_inc = False
            else:
                if prev_n < next_n:
                    return False

        return not is_inc

