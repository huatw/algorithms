class Solution:
    def pivotIndex(self, nums):
        left_sum, right_sum = [], []
        total = 0
        for n in nums:
            left_sum.append(total)
            total += n

        total = 0
        for n in nums[::-1]:
            right_sum.append(total)
            total += n

        right_sum = right_sum[::-1]

        for i, (left, right) in enumerate(zip(left_sum, right_sum)):
            if left == right:
                return i

        return -1