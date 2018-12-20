class Solution:
    def numBusesToDestination(self, routes, S, T):
        if S == T:
            return 0

        routes = [set(route) for route in routes]
        route_map = collections.defaultdict(list)
        for i, route in enumerate(routes):
            for j in range(i + 1, len(routes)):
                if any(r in routes[j] for r in route):
                    route_map[i].append(j)
                    route_map[j].append(i)

        seen, ends = set(), set(i for i, route in enumerate(routes) if T in route)
        dq = collections.deque((i, 1) for i, route in enumerate(routes) if S in route)

        while dq:
            i, depth = dq.popleft()
            if i in ends:
                return depth
            if i in seen:
                continue
            seen.add(i)
            for next_i in route_map[i]:
                dq.append((next_i, depth + 1))

        return -1