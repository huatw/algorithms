class RandomizedSet:
    def __init__(self):
        self.l = []
        self.m = {}


    def insert(self, val):
        if val not in self.m:
            self.l.append(val)
            self.m[val] = len(self.l) - 1
            return True

        return False


    # exchange val and the last in list
    def remove(self, val):
        if val in self.m:
            idx, last = self.m[val], self.l[-1]
            self.l[idx] = last
            self.m[last] = idx
            self.m.pop(val)
            self.l.pop()
            return True

        return False


    def getRandom(self):
        return self.l[random.randint(0, len(self.l) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()