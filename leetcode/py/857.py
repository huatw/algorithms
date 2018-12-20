class Solution:
    def mincostToHireWorkers(self, quality, wage, K):
        workers = sorted((w / q, q, w) for q, w in zip(quality, wage))
        res = float('inf')
        hq = []
        sumq = 0

        for ratio, q, w in workers:
            sumq += q
            heapq.heappush(hq, -q)

            if K < len(hq):
                sumq += heapq.heappop(hq)

            if K == len(hq):
                res = min(res, sumq * ratio)

        return res
