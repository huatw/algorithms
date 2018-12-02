'''
0----1
| \  |
|  \ |
3----2
0: 1, 2, 3
1: 0, 2
2: 0, 1, 3
3: 0, 2
0----1
|    |
|    |
3----2
0: 1, 3
1: 0, 2
3: 0, 2
2: 3, 1
'''
class Solution:
    def isBipartite(self, graph):
        node_map = collections.defaultdict(list)

        for n1, n2s in enumerate(graph):
            for n2 in n2s:
                node_map[n1].append(n2)
                node_map[n2].append(n1)

        while node_map:
            start_node, level = node_map.popitem()
            n_set1, n_set2 = set([start_node]), set()

            while level:
                n_set1, n_set2 = n_set2, n_set1
                next_level = []
                for node in level:
                    if node in n_set2:
                        return False
                    if node not in n_set1:
                        n_set1.add(node)
                        next_level.extend(node_map.pop(node))
                level = next_level

        return True




class Solution:
    def isBipartite(self, graph):
        values = {}

        def dfs(point_a, points):
            for point_b in points:
                if point_b in values: # visited, check color
                    if values[point_b] == values[point_a]:
                        return False
                else: # add opposite color and visit
                    values[point_b] = not values[point_a]
                    if not dfs(point_b, graph[point_b]):
                        return False
            return True

        for point_a, points in enumerate(graph):
            if point_a not in values:
                values[point_a] = True
                if not dfs(point_a, points):
                    return False

        return True
