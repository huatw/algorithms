# klog(n)
class Solution:
    def kthSmallest(self, matrix, k):
        hq = [(row[0], i, 0) for i, row in enumerate(matrix) if row]
        heapq.heapify(hq)

        for _ in range(k):
            res, i, j = heapq.heappop(hq)
            if j + 1 < len(matrix[i]):
                heapq.heappush(hq, (matrix[i][j + 1], i, j + 1))

        return res

# nlog(k)
# ?


# O(n) ?
