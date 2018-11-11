
class Solution:
    def getSkyline(self, buildings):
        # events : left in, right in, image there is a moving line in y axis
        events = sorted([(L, -H, R) for L, R, H in buildings] + list({(R, 0, None) for _, R, _ in buildings}))
        res = [[0, 0]] # start of events
        hp = [(0, float("inf"))] # end of events

        for x, neg_h, R in events:
            while x >= hp[0][1]: # pop outdated R
                heapq.heappop(hp)
            if neg_h: # every in event
                heapq.heappush(hp, (neg_h, R)) # so only bigger height visible
            if res[-1][1] != -hp[0][0]: # for every event, check last height(res) and current visible height(hp)
                res.append([x, -hp[0][0]])

        return res[1:]