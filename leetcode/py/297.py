# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        res = ''
        dq = collections.deque([root])

        while dq:
            node = dq.popleft()
            if not node:
                res += ',None'
            else:
                res += ',' + str(node.val)
                dq.append(node.left)
                dq.append(node.right)

        return res

    def deserialize(self, data):
        data = collections.deque(data.split(','))
        _, val = data.popleft(), data.popleft()
        root = None if val == 'None' else TreeNode(int(val))
        dq = collections.deque([root])

        while dq:
            node = dq.popleft()
            if node:
                left, right = data.popleft(), data.popleft()
                node.left = TreeNode(int(left)) if left != 'None' else None
                node.right = TreeNode(int(right)) if right != 'None' else None
                dq.append(node.left)
                dq.append(node.right)

        return root
