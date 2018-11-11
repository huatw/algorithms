# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
class Solution:
    def cloneGraph(self, node):
        node_copy_map = {None: None}

        def dfs(node):
            if node not in node_copy_map:
                node_copy = UndirectedGraphNode(node.label)
                node_copy_map[node] = node_copy
                node_copy.neighbors = [dfs(child) for child in node.neighbors]
            return node_copy_map[node]

        return dfs(node)


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