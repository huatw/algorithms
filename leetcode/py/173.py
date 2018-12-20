class BSTIterator(object):
    def __init__(self, root):
        self.cur = root
        self.val = None

    def hasNext(self):
        if not self.cur:
            return False

        if self.cur.left:
            prev = self.cur.left
            while prev.right:
                prev = prev.right
            prev.right = self.cur
            temp = self.cur
            self.cur = self.cur.left
            temp.left = None
            return self.hasNext()
        else:
            self.val = self.cur.val
            self.cur = self.cur.right
            return True

    def next(self):
        return self.val




class BSTIterator(object):
    def gen(self, node):
        if not node:
            return
        # yield from self.gen(node.left)
        for val in self.gen(node.left):
            yield val
        yield node.val
        # yield from self.gen(node.right)
        for val in self.gen(node.right):
            yield val

    def __init__(self, root):
        self.val = None
        self.g = self.gen(root)

    def hasNext(self):
        self.val = next(self.g, None)
        return False if self.val == None else True

    def next(self):
        return self.val