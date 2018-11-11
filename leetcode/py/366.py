"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
'''
   1
  2 3
 4 5
[4, 5] [2] [3]
node_height = max(h(node.left), h(node.right)) + 1
'''

# iter
class Solution:
    def findLeaves(self, root):
        if not root:
            return []
        height_nodes_map = collections.defaultdict(list)
        max_height = 0

        stack = [[root, 0, False, 0]] # node, height, is_traversed, offset
        while stack:
            node, height, is_traversed, offset = stack[-1]
            if is_traversed:
                # pop and update parent height
                height_nodes_map[height].append(node.val)
                stack.pop()
                if offset:
                    stack[offset][1] = max(stack[offset][1], height + 1)
                else:
                    max_height = height
            else:
                stack[-1][2] = True
                offset = -1
                if node.left:
                    stack.append([node.left, 0, False, offset])
                    offset -= 1
                if node.right:
                    stack.append([node.right, 0, False, offset])

        res = [height_nodes_map[i] for i in range(max_height + 1)]
        return res



# recursive
class Solution:
    def findLeaves(self, root):
        if not root:
            return []
        height_nodes_map = collections.defaultdict(list)
        max_height = 0

        def build_map(node):
            nonlocal max_height
            if not node:
                return -1
            height = max(build_map(node.left), build_map(node.right)) + 1
            max_height = max(max_height, height)
            height_nodes_map[height].append(node.val)
            return height

        build_map(root)

        res = [height_nodes_map[i] for i in range(max_height + 1)]
        return res
