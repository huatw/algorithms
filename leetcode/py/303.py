class NumArray:
    def __init__(self, nums):
        self.totals = [0]
        for num in nums:
            self.totals.append(self.totals[-1] + num)

    def sumRange(self, i, j):
        return self.totals[j + 1] - self.totals[i]


class NumArray:
    def __init__(self, nums):
        self.res = {-1: 0, 0: 0}

        for i, n in enumerate(nums):
            self.res[i] = self.res[i-1] + n


    def sumRange(self, i, j):
        return self.res[j] - self.res[i-1]
