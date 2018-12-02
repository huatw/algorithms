# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

'''
     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \  / \
4->5->6->7 -> NULL
'''
# stack based BFS
class Solution:
    def connect(self, root):
        if not root:
            return

        level = [root]

        while level:
            next_level = []
            for i, node in enumerate(level):
                if i + 1 < len(level):
                    node.next = level[i + 1]
                next_level.extend([node.left, node.right])
            level = next_level


# O(1) space
class Solution:
    def connect(self, root):
        if not root:
            return

        while root.left:
            cur = root
            while cur:
                right = cur.right
                cur.left.next = right
                cur = cur.next
                if cur and right:
                    right.next = cur.left

            root = root.left


# bfs O(1)
class Solution:
    def connect(self, root):
        def bfs(head):
            if not head or not head.left:
                return
            cur = head
            while cur:
                left, right = cur.left, cur.right
                cur = cur.next
                left.next = right
                if cur:
                    right.next = cur.left
            bfs(head.left) # tail

        bfs(root)


class Solution:
    def connect(self, root):
        head = root
        while head and head.left:
            cur = head
            while cur:
                left, right = cur.left, cur.right
                cur = cur.next
                left.next = right
                if cur:
                    right.next = cur.left
            head = head.left
