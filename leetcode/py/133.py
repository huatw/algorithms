# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return node

        stack = [node]
        root = UndirectedGraphNode(node.label)
        dct = {node.label: root}

        while stack:
            top = stack.pop()
            for n in top.neighbors:
                if n.label not in dct:
                    stack.append(n)
                    dct[n.label] = UndirectedGraphNode(n.label)
                dct[top.label].neighbors.append(dct[n.label])

        return root