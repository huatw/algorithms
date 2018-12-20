add, diff, mul, div = lambda a, b : a + b, lambda a, b : a - b, lambda a, b : a * b, lambda a, b : a / b
class Solution:
    def judgePoint24(self, nums):
        if not nums:
            return False

        if len(nums) == 1:
            return abs(nums[0] - 24) < 1e-6

        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums):
                if i == j:
                    continue
                rest = [n for k, n in enumerate(nums) if k != i and k != j]
                for op in [add, diff, mul, div]:
                    if (op == div and num2 == 0) or (i > j and op in [add, mul]):
                        continue
                    rest.append(op(num1, num2))
                    if self.judgePoint24(rest):
                        return True
                    rest.pop()

        return False


from operator import truediv, mul, add, sub

class Solution:
    def judgePoint24(self, nums):
        if not nums:
            return False
        N = len(nums)
        if N == 1:
            return abs(nums[0] - 24) < 1e-6

        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                rest = [nums[k] for k in range(N) if k != i and k != j]
                for op in (truediv, mul, add, sub):
                    if (op in [mul, add] and j > i) or (op == truediv and nums[j] == 0):
                        continue
                    rest.append(op(nums[i], nums[j]))
                    if self.judgePoint24(rest):
                        return True
                    rest.pop()

        return False
