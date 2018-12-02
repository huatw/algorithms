class Solution:
    def __init__(self, w):
        self.w = []
        for n in w:
            self.w.append(n + (self.w[-1] if self.w else 0))

    def pickIndex(self):
        def bisect_left(nums, n):
            lo, hi = 0, len(nums) - 1
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if n > nums[mid]:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        random_i = random.randint(1, self.w[-1])
        return bisect_left(self.w, random_i)



class Solution:
    # O(n)
    def __init__(self, w):
        self.w = list(itertools.accumulate(w))
    #O(logn)
    def pickIndex(self):
        return bisect.bisect_left(self.w, random.randint(1, self.w[-1]))



# space limitation
class Solution:
    def __init__(self, w):
        self.lst = [n for n, size in enumerate(w) for _ in range(size)]

    def pickIndex(self):
        return self.lst[math.floor(random.random() * len(self.lst))]
