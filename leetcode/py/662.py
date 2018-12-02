'''
           1
         /   \
        2     3
       / \     \
      4   5     7

'''
# iter BFS
class Solution:
    def widthOfBinaryTree(self, root):
        if not root:
            return 0

        res = 0
        level = [(root, 1)]
        while level:
            res = max(res, level[-1][1] - level[0][1])
            next_level = []

            for (node, num) in level:
                if node.left:
                    next_level.append((node.left, num * 2))
                if node.right:
                    next_level.append((node.right, num * 2 + 1))

            level = next_level

        return res + 1
