class NumArray(object):

    def __init__(self, nums):
        self.res = {-1: 0, 0: 0}

        for i, n in enumerate(nums):
            self.res[i] = self.res[i-1] + n


    def sumRange(self, i, j):
        return self.res[j] - self.res[i-1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)