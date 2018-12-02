'''
        10
    5       15
1      6  13    16
10 5 1 6 15 13 16

'''
class Codec:
    def serialize(self, root):
        vals = []
        def pre_order_traversal(node):
            if node:
                vals.append(str(node.val))
                pre_order_traversal(node.left)
                pre_order_traversal(node.right)
        pre_order_traversal(root)
        return ' '.join(vals)

    def deserialize(self, data):
        vals = collections.deque(int(val) for val in data.split())
        def build_tree(min_val, max_val):
            if vals and min_val < vals[0] < max_val:
                val = vals.popleft()
                node = TreeNode(val)
                node.left = build_tree(min_val, val)
                node.right = build_tree(val, max_val)
                return node

        return build_tree(-float('inf'), float('inf'))
