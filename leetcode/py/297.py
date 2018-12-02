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




class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    def __str__(self):
        return '(' + str(self.val) + ',' + str(self.left) + ',' + str(self.right) + ')'
def tokenize(s):
    tokens = []
    token = ''
    for ch in s:
        if ch in ['(', ')', ',']:
            if token:
                tokens.append(token)
                token = ''
            tokens.append(ch)
        else:
            token += ch
    return tokens
def parse(tokens): # => [22, [33, N, N], [44, N, N]]
    stacks = [[]]
    for token in tokens:
        if token == '(':
            stacks.append([])
        elif token == ')':
            sub_stack = stacks.pop()
            stacks[-1].append(sub_stack)
        elif token == ',':
            continue
        else: # N or number
            stacks[-1].append(token)
    return stacks[-1][-1]
def build_tree(ast):
    if isinstance(ast, list):
        root, left, right = ast
        node = Node(int(root))
        node.left = build_tree(left)
        node.right = build_tree(right)
    elif ast == 'N':
        node = None
    else:
        node = Node(int(root))
    return node
def decode_tree(s):
    tokens = tokenize(s)
    ast = parse(tokens)
    t = build_tree(ast)
    return t

node = decode_tree("(22,(33,N,(555,N,N)),(44,N,N))")





class Codec:
    def serialize(self, root):
        if not root:
            return 'None'
        return '(' + str(root.val) + ',' + self.serialize(root.left) + ',' + self.serialize(root.right) + ')'

    def deserialize(self, data):
        def tokenize(s):
            tokens = []
            token = ''
            for ch in s:
                if ch in '(),':
                    if token:
                        tokens.append(token)
                        token = ''
                    tokens.append(ch)
                else:
                    token += ch
            if token:
                tokens.append(token)
            return tokens

        def parse(tokens):
            stacks = [[]]
            for token in tokens:
                if token == '(':
                    stacks.append([])
                elif token == ')':
                    substack = stacks.pop()
                    stacks[-1].append(substack)
                elif token == ',':
                    pass
                else:
                    stacks[-1].append(token)
            return stacks[-1][-1]

        def build_tree(ast):
            if isinstance(ast, str):
                return None if ast == 'None' else TreeNode(int(ast))
            val, left, right = ast
            root = build_tree(val)
            root.left = build_tree(left)
            root.right = build_tree(right)
            return root

        tokens = tokenize(data)
        ast = parse(tokens)
        res = build_tree(ast)
        return res
