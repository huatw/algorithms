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
        head = root
        while head:
            next_head, prev_child = None, None
            while head:
                for child in [head.left, head.right]:
                    if child:
                        if not next_head:
                            next_head = child
                        else:
                            prev_child.next = child
                        prev_child = child
                head = head.next
            head = next_head


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


