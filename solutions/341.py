class NestedIterator(object):

    def __init__(self, nestedList):
        self.stack = nestedList

    def next(self):
        first = self.stack[0]
        self.stack = self.stack[1:]
        # first, *self.stack = self.stack
        return first.getInteger()

    def hasNext(self):
        if len(self.stack) > 0:
            if self.stack[0].isInteger():
                return True
            self.stack = self.stack[0].getList() + self.stack[1:]
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


