# iter
class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0

        level = [root]
        depth = 0

        while level:
            depth += 1
            newLevel = []

            for node in level:
                if not node.left and not node.right:
                    return depth
                if node.left:
                    newLevel.append(node.left)
                if node.right:
                    newLevel.append(node.right)
            level = newLevel

        return depth




# iter
class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0

        def recur(level, depth = 1):
            newLevel = []

            for node in level:
                if not node.left and not node.right:
                    return depth
                if node.left:
                    newLevel.append(node.left)
                if node.right:
                    newLevel.append(node.right)

            return recur(newLevel, depth + 1)

        return recur([root])




