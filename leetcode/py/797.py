# DFS O(n) O(n2)
class Solution:
    def allPathsSourceTarget(self, graph):
        path_map = {}

        def recur(start):
            if start not in path_map:
                if graph[start]:
                    paths = [[start] + path for node in graph[start] for path in recur(node)]
                else:
                    paths = [[start]]
                path_map[start] = paths

            return path_map[start]

        return recur(0)




class Solution:
    def allPathsSourceTarget(self, graph):
        path_map = {}
        stack = [(0, False)]
        while stack:
            start, is_traversed = stack.pop()
            if graph[start]:
                if is_traversed:
                    path_map[start] = [[start] + path for node in graph[start] for path in path_map[node]]
                else:
                    stack.append((start, True))
                    for node in graph[start]:
                        stack.append((node, False))
            else:
                path_map[start] = [[start]]

        return path_map[0]