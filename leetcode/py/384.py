class Solution:
    def __init__(self, nums):
        self.nums_cp = nums
        self.nums = [*nums]


    def reset(self):
        self.nums = [*self.nums_cp]
        return self.nums


    def shuffle(self):
        for i in range(len(self.nums), 0, -1):
            idx = math.floor(random.random() * i)
            self.nums[idx], self.nums[i - 1] = self.nums[i - 1], self.nums[idx]

        return self.nums
