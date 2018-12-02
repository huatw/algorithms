class TwoSum:
    def __init__(self):
        self.num_map = collections.defaultdict(int)

    def add(self, num):
        self.num_map[num] += 1

    def find(self, val):
        for num in self.num_map:
            if val - num == num:
                if self.num_map[num] > 1:
                    return True
            elif val - num in self.num_map:
                return True
        return False