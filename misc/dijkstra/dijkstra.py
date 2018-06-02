from collections import defaultdict
from queue import PriorityQueue


class Graph():
    def __init__(self, edges):
        self.starts = set([start for start, _, _ in edges])
        self.neighbours = defaultdict(list)
        for start, end, cost in edges:
            self.neighbours[start].append((end, cost))

    def dijkstra(self, start, end):
        assert start in self.starts

        prev_paths = defaultdict(lambda: None)
        prev_costs = defaultdict(lambda: float('inf'))
        prev_costs[start] = 0
        point = start

        while point and point != end:
            for next_point, cost in self.neighbours[point]:
                next_cost = prev_costs[point] + cost
                if next_cost < prev_costs[next_point]:
                    prev_costs[next_point] = next_cost
                    prev_paths[next_point] = point
            prev_costs.pop(point)
            point = min(prev_costs, key=prev_costs.get)

        paths = []
        while point:
            paths.append(point)
            point = prev_paths[point]

        return (prev_costs[end], list(reversed(paths)))


graph = Graph([("a", "b", 7),  ("a", "c", 9),  ("a", "f", 14), ("b", "c", 10), ("b", "d", 15), ("c", "d", 11), ("c", "f", 2),  ("d", "e", 6), ("e", "f", 9)])

res = graph.dijkstra("a", "e")
print(res)
