# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
Input:

   1
    \
     3
    /
   2

Output:
1

=> in order: [-5, -3, 1, 4]
'''
# O(n) O(n)
class Solution:
    def getMinimumDifference(self, root):
        lst = []
        def in_order_traversal(node):
            if not node:
                return
            in_order_traversal(node.left)
            lst.append(node.val)
            in_order_traversal(node.right)

        in_order_traversal(root)

        res = float('inf')
        for prev_val, next_val in zip(lst, lst[1:]):
            res = min(res, next_val- prev_val)
        return res




# O(n) O(1)
class Solution:
    def getMinimumDifference(self, root):
        res = float('inf')
        prev_val = -float('inf')

        def in_order_traversal(node):
            nonlocal res, prev_val
            if not node:
                return
            in_order_traversal(node.left)
            res = min(res, node.val - prev_val)
            prev_val = node.val
            in_order_traversal(node.right)

        in_order_traversal(root)
        return res




