class ZigzagIterator(object):
    def __init__(self, v1, v2):
        self.vs = [v1, v2]
        self.ps = [0, 0]
        self.cur = -1

    def next(self):
        self.cur = (self.cur + 1) % len(self.vs)
        while self.ps[self.cur] == len(self.vs[self.cur]):
            self.cur = (self.cur + 1) % len(self.vs)
        val = self.vs[self.cur][self.ps[self.cur]]
        self.ps[self.cur] += 1
        return val

    def hasNext(self):
        return any(p < len(v) for v, p in zip(self.vs, self.ps))



# n items
class ZigzagIterator(object):
    def __init__(self, vs):
        self.vs = vs
        self.ps = [0] * len(vs)
        self.cur = -1

    def next(self):
        self.cur = (self.cur + 1) % len(self.vs)
        while self.ps[self.cur] == len(self.vs[self.cur]):
            self.cur = (self.cur + 1) % len(self.vs)
        val = self.vs[self.cur][self.ps[self.cur]]
        self.ps[self.cur] += 1
        return val

    def hasNext(self):
        return any(p < len(v) for v, p in zip(self.vs, self.ps))
