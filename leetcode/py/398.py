# O(1) O(n)
class Solution:
    def __init__(self, nums):
        self.nums = nums

    def pick(self, target):
        return random.choice([k for k, v in enumerate(self.nums) if v == target])


# O(n) O(1)
class Solution:
    def __init__(self, nums):
        self.d = collections.defaultdict(list)
        for i, num in enumerate(nums):
            self.d[num].append(i)

    def pick(self, target):
        if target in self.d:
            return self.d[target][math.floor(random.random() * len(self.d[target]))]

