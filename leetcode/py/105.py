# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
    3
   / \
  9  20
    /  \
   15   7
preorder = [3,  9,  20,15,7]
inorder =  [9,  3,  15,20,7]
'''

class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return

        root_val = preorder[0]
        root = TreeNode(root_val)

        for i, val in enumerate(inorder):
            if root_val == val:
                break
        left_in_order, right_in_order = inorder[:i], inorder[i + 1:]
        left_pre_order, right_pre_order = preorder[1:i + 1], preorder[i + 1:]
        root.left = self.buildTree(left_pre_order, left_in_order)
        root.right = self.buildTree(right_pre_order, right_in_order)

        return root





class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder:
            return

        root = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:idx + 1], inorder[:idx])
        root.right = self.buildTree(preorder[idx + 1:], inorder[idx + 1:])

        return root