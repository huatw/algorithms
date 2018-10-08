# n bucket
class Solution:
    def topKFrequent(self, nums, k):
        num_map = collections.Counter(nums) # n
        cnt_map = collections.defaultdict(list)

        for num, cnt in num_map.items(): # n
            cnt_map[cnt].append(num)

        res = []
        for cnt in range(len(nums), 0, -1): # n
            for num in cnt_map[cnt]:
                res.append(num)
                if len(res) == k:
                    return res

# nlogk
class Solution:
    def topKFrequent(self, nums, k):
        hq = []

        num_map = collections.Counter(nums)

        for num, cnt in num_map.items():
            if len(hq) == k:
                heapq.heappushpop(hq, (cnt, num))
            else:
                heapq.heappush(hq, (cnt, num))

        return list(map(lambda p: p[1], hq))


class Solution:
    def topKFrequent(self, nums, k):
        return [k for k, v in collections.Counter(nums).most_common(k)]

