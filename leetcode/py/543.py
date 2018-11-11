# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        res = 0

        def recur(node):
            nonlocal res
            if not node:
                return -1
            left_dis, right_dis = recur(node.left) + 1, recur(node.right) + 1
            res = max(res, left_dis + right_dis)
            return max(left_dis, right_dis)

        recur(root)

        return res