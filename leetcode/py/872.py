import itertools

class Solution:
    def leafSimilar(self, root1, root2):
        def gen_leaves(node):
            if not node:
                return
            if not node.left and not node.right:
                yield node.val
            yield from gen_leaves(node.left)
            yield from gen_leaves(node.right)

        return all(v1 == v2 for v1, v2 in \
            itertools.zip_longest(gen_leaves(root1), gen_leaves(root2)))
