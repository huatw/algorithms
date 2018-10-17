# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        def recur(node, next_node):
            if not node:
                return next_node
            if node.left and not node.right:
                node.right = recur(node.left, next_node)
                node.left = None
            elif not node.left and node.right:
                recur(node.right, next_node)
            elif node.left and node.right:
                node.right = recur(node.left, recur(node.right, next_node))
                node.left = None
            else:
                node.right = next_node
            return node

        recur(root, None)



class Solution:
    def flatten(self, root):
        cur = root
        while cur:
            if cur.left:
                temp = cur.left
                while temp.right:
                    temp = temp.right
                temp.right = cur.right
                cur.right = cur.left
                cur.left = None
            cur = cur.right

