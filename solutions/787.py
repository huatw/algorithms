class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        m = collections.defaultdict(dict)
        for start, end, price in flights:
            m[start][end] = price

        res = {src: 0}
        nowMin = float('inf')
        for _ in range(K + 1):
            newRes = collections.defaultdict(lambda: float('inf'), res)
            for start, total_price in res.items():
                for end, price in m[start].items():
                    if total_price + price < nowMin:
                        newRes[end] = min(total_price + price, newRes[end])
                        if end == dst:
                            nowMin = newRes[end]

            res = newRes

        return nowMin if nowMin != float('inf') else -1


