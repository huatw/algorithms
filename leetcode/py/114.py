# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        def helper(node, next_node):
            left, right = node.left, node.right
            if left and not right:
                node.right = helper(left, next_node)
                node.left = None
            elif not left and right:
                helper(right, next_node)
            elif not left and not right:
                node.right = next_node
            else:
                node.right = helper(left, helper(right, next_node))
                node.left = None
            return node

        if not root:
            return
        helper(root, None)




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

