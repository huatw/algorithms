# using hq
import collections
import heapq

def dijkstra(edges, f, t):
    edge_map = collections.defaultdict(list)
    costs = collections.defaultdict(lambda: float('inf'), {f: 0})
    seen = set()
    hq = [(0, f, [f])]

    for v1, v2, cost in edges:
        edge_map[v1].append((v2, cost))
        edge_map[v2].append((v1, cost))

    while hq:
        cost, v1, path = heapq.heappop(hq)
        if v1 in seen:
            continue
        seen.add(v1)
        if v1 == t:
            return (cost, path)
        for v2, next_cost in edge_map[v1]:
            if v2 in seen:
                continue
            if cost + next_cost < costs[v2]:
                costs[v2] = cost + next_cost
                heapq.heappush(hq, (costs[v2], v2, [*path, v2]))

    return (float("inf"), [])

edges = [("a", "b", 7),  ("a", "c", 9),  ("a", "f", 14), ("b", "c", 10), ("b", "d", 15), ("c", "d", 11), ("c", "f", 2),  ("d", "e", 6), ("e", "f", 9)]
dijkstra(edges, "a", "e")
