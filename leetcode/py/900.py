class RLEIterator:
    def __init__(self, nums):
        self.nums = nums
        self.cur_pointer = 0
        self.cnt = 0

    def next(self, n):
        if self.cur_pointer >= len(self.nums):
            return -1
        if self.cnt + n > self.nums[self.cur_pointer]:
            next_n = self.cnt + n - self.nums[self.cur_pointer]
            self.cnt = 0
            self.cur_pointer += 2
            return self.next(next_n)
        self.cnt += n
        return self.nums[self.cur_pointer + 1]

