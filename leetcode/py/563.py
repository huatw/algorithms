# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
     1
  2     3
4   5  6  7
'''
class Solution:
    def findTilt(self, root):
        total = 0
        def recur(node):
            nonlocal total
            if not node:
                return 0
            left_sum, right_sum = recur(node.left), recur(node.right)
            total += abs(left_sum - right_sum)
            return left_sum + right_sum + node.val

        recur(root)
        return total


# iter
class Solution:
    def findTilt(self, root):
        if not root:
            return 0
        res = 0
        sum_map = { None: 0 }
        stack = [(root, False)]

        while stack:
            node, is_traversed = stack.pop()
            if is_traversed:
                sum_map[node] = sum_map[node.left] + sum_map[node.right] + node.val
                res += abs(sum_map[node.left] - sum_map[node.right])
            else:
                stack.append((node, True))
                if node.left:
                    stack.append((node.left, False))
                if node.right:
                    stack.append((node.right, False))

        return res
