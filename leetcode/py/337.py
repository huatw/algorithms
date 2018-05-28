# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        cache = {}
        def recur(node):
            if node in cache:
                return cache[node]

            if not node:
                return 0

            res1 = node.val

            if node.left:
                res1 += recur(node.left.left) + recur(node.left.right)
            if node.right:
                res1 += recur(node.right.left) + recur(node.right.right)

            res2 = recur(node.left) + recur(node.right)
            res = max(res1, res2)
            cache[node] = res

            return res

        return recur(root)




class Solution(object):
    def rob(self, root):
        def superrob(node):
            if not node:
                return (0, 0)

            left, right = superrob(node.left), superrob(node.right)
            now = node.val + left[1] + right[1]
            later = max(left) + max(right)

            return (now, later) # rob now or later

        return max(superrob(root))



