
class Solution:
    def findSecondMinimumValue(self, root):
        if not root:
            return -1

        min_val = root.val
        res = float('inf')
        q = [root]

        while q:
            node = q.pop()
            if not node.left or not node.right:
                continue
            if node.left.val < node.right.val:
                q.append(node.left)
                res = min(res, node.right.val)
            elif node.left.val > node.right.val:
                q.append(node.right)
                res = min(res, node.left.val)
            else:
                q.append(node.left)
                q.append(node.right)

        return res if res != float('inf') else -1

class Solution:
    def findSecondMinimumValue(self, root):
        min_val = root.val
        res = float('inf')

        def dfs(node):
            nonlocal res
            if not node:
                return
            if min_val < node.val < res:
                res = node.val
            else:
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return res if res != float('inf') else -1

class Solution:
    def findSecondMinimumValue(self, root):
        min_val = root.val
        res = float('inf')

        def dfs(node):
            nonlocal res
            if not node or not node.left or not node.right:
                return
            if node.left.val < node.right.val:
                res = min(res, node.right.val)
                dfs(node.left)
            elif node.left.val > node.right.val:
                res = min(res, node.left.val)
                dfs(node.right)
            else:
                dfs(node.left)
                dfs(node.right)

        dfs(root)

        return res if res != float('inf') else -1
