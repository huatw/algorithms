class Solution:
    def networkDelayTime(self, times, N, K):
        graph = collections.defaultdict(list)
        for from_node, to_node, distance in times:
            graph[from_node].append((distance, to_node))

        hq = [(0, K)]
        node_distance_map = {}
        while hq:
            distance, node = heapq.heappop(hq)
            if node in node_distance_map:
                continue
            node_distance_map[node] = distance
            for next_distance, next_node in graph[node]:
                if next_node not in node_distance_map:
                    heapq.heappush(hq, (distance + next_distance, next_node))

        return max(node_distance_map.values()) if N == len(node_distance_map) else -1

