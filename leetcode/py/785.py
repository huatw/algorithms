class Solution:
    def isBipartite(self, graph):
        values = {}

        def dfs(point_a, points):
            for point_b in points:
                if point_b in values:
                    if values[point_b] == values[point_a]:
                        return False
                else:
                    values[point_b] = 1 - values[point_a]
                    if not dfs(point_b, graph[point_b]):
                        return False
            return True

        for point_a, points in enumerate(graph):
            if point_a not in values:
                values[point_a] = 0
                if not dfs(point_a, points):
                    return False

        return True