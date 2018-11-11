# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \
     3   1

'''
class Solution:
    def rob(self, root):
        cache = {None: 0}

        def recur(node):
            if node not in cache:
                children_sum = recur(node.left) + recur(node.right)
                grand_children_sum = node.val
                if node.left:
                    grand_children_sum += recur(node.left.left) + recur(node.left.right)
                if node.right:
                    grand_children_sum += recur(node.right.left) + recur(node.right.right)
                cache[node] = max(children_sum, grand_children_sum)
            return cache[node]

        return recur(root)




class Solution:
    def rob(self, root):
        def superrob(node):
            if not node:
                return (0, 0)

            left, right = superrob(node.left), superrob(node.right)
            now = node.val + left[1] + right[1]
            later = max(left) + max(right)

            return (now, later) # rob now or later

        return max(superrob(root))



