class NestedIterator(object):
    def __init__(self, nestedList):
        self.dq = collections.deque(nestedList)

    def next(self):
        return self.dq.popleft().getInteger()

    def hasNext(self):
        if not self.dq:
            return False
        if self.dq[0].isInteger():
            return True
        self.dq.extendleft(self.dq.popleft().getList()[::-1])
        return self.hasNext()




class NestedIterator(object):
    def __init__(self, nestedList):
        self.stack = nestedList[::-1]

    def next(self):
        return self.stack.pop().getInteger()

    def hasNext(self):
        if self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            self.stack.extend(self.stack.pop().getList()[::-1])
            return self.hasNext()
        return False


class NestedIterator(object):
    def __init__(self, nestedList):
        def gen():
            for nested in nestedList:
                if nested.isInteger():
                    yield nested.getInteger()
                else:
                    # yield from gen(nested.getList())
                    for nstd in gen(nested.getList()):
                        yield nstd

        self.gen = gen()

    def next(self):
        return self.val

    def hasNext(self):
        try:
            self.val = next(self.gen)
            return True
        except StopIteration:
            return False