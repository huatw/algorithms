# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
'''
     1
   /  \
  2    3
 / \    \
4   5    7

     1 -> NULL
   /  \
  2 -> 3 -> NULL     parent
 / \    \
4-> 5 -> 7 -> NULL   next_parent child
'''
# Space O(1)
class Solution:
    def connect(self, root):
        if not root:
            return
        parent, next_parent, child = root, None, None

        while parent:
            while parent:
                if parent.left:
                    if not next_parent:
                        next_parent = parent.left
                    if child:
                        child.next = parent.left
                    child = parent.left
                if parent.right:
                    if not next_parent:
                        next_parent = parent.right
                    if child:
                        child.next = parent.right
                    child = parent.right
                parent = parent.next
            parent, next_parent, child = next_parent, None, None




# BFS
class Solution:
    def connect(self, root):
        if not root:
            return
        level = [root]

        while level:
            for prev_node, next_node in zip(level, level[1:]):
                prev_node.next = next_node
            next_level = []
            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            level = next_level



