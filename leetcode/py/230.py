class Solution:
    def kthSmallest(self, root, k):
        def preorder(node):
            if not node:
                return
            yield from preorder(node.left)
            yield node.val
            yield from preorder(node.right)

        for val in preorder(root):
            k -= 1
            if k == 0:
                return val


# recursion
class Solution:
    def kthSmallest(self, root, k):
        self.k = k
        self.res = None
        self.recur(root)
        return self.res


    def recur(self, node):
        if not node:
            return

        self.recur(node.left)

        if self.res is not None:
            return

        self.k -= 1
        if self.k == 0:
            self.res = node.val
            return

        self.recur(node.right)




# generator
class Solution:
    def kthSmallest(self, root, k):
        return next(itertools.islice(self.inorder(root), k-1, k))
        # for i, node in enumerate(self.gen(root)):
        #     if i+1 == k:
        #         return node.val


    def gen(self, node):
        if not node:
            return

        yield from self.gen(node.left) # NOTE: gen has yield, so it is a generator
        yield node
        yield from self.gen(node.right)



