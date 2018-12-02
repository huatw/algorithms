'''
Example 1:

        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
The following are two duplicate subtrees:

      2
     /
    4
and

    4
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findDuplicateSubtrees(self, root):
        node_str_map = {None: 'N'}
        def serialize_tree(node):
            if node not in node_str_map:
                node_str_map[node] = '(' + str(node.val) + ',' + serialize_tree(node.left) + ',' + serialize_tree(node.right) + ')'
            return node_str_map[node]

        serialize_tree(root)
        str_node_map = collections.defaultdict(list)

        for (node, serialize_tree) in node_str_map.items():
            str_node_map[serialize_tree].append(node)

        return [node_list[0] for node_list in str_node_map.values() if len(node_list) > 1]




class Solution:
    def findDuplicateSubtrees(self, root):
        str_node_map = collections.defaultdict(list)

        def serialize_tree(node):
            if not node:
                return 'None'
            serialize_str = '(' + str(node.val) + ',' + serialize_tree(node.left) + ',' + serialize_tree(node.right) + ')'
            str_node_map[serialize_str].append(node)
            return serialize_str

        serialize_tree(root)
        return [node_list[0] for node_list in str_node_map.values() if len(node_list) > 1]

