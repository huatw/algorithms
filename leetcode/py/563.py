# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root):
        def recur(node):
            left_tilt, left_sum = recur(node.left) if node.left else (0, 0)
            right_tilt, right_sum = recur(node.right) if node.right else (0, 0)
            cur_tilt = left_tilt + right_tilt + abs(left_sum - right_sum)
            cur_sum = left_sum + right_sum + node.val
            return (cur_tilt, cur_sum)

        return recur(root)[0]