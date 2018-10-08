class RandomizedSet:
    def __init__(self):
        self.lst = []
        self.hmap = {}

    def insert(self, val):
        if val in self.hmap:
            return False
        self.hmap[val] = len(self.lst)
        self.lst.append(val)
        return True

    def remove(self, val):
        if val not in self.hmap:
            return False
        last_val, idx = self.lst[-1], self.hmap[val]
        self.hmap[last_val] = idx
        self.lst[idx] = last_val
        self.lst.pop()
        # notice here cannot pop before, duplication
        self.hmap.pop(val)
        return True

    def getRandom(self):
        idx = math.floor(random.random() * len(self.hmap))
        return self.lst[idx]

# {}
# [] random read through index
# { val: index } <=> [val]
# insert O(1)
# delete O(1)
# get_random O(1) ?
# support random : random function => ordered structure: list


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