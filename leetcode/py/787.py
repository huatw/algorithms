class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        f_t_map = collections.defaultdict(list)
        for f, t, price in flights:
            f_t_map[f].append((t, price))

        hq = [(0, src, 0)]
        while hq:
            acc_price, f, k = heapq.heappop(hq)
            if f == dst:
                return acc_price
            if k > K:
                continue
            for t, price in f_t_map[f]:
                heapq.heappush(hq, (acc_price + price, t, k + 1))
        return -1

