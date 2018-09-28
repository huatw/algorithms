# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        prev, level_head = None, None
        # up to dwon
        while root:
            while root:
                if root.left:
                    if level_head:
                        prev.next = root.left
                    else:
                        level_head = root.left
                    prev = root.left
                if root.right:
                    if level_head:
                        prev.next = root.right
                    else:
                        level_head = root.right
                    prev = root.right
                root = root.next

            root = level_head
            prev = None
            level_head = None

