import collections, bisect

class TopVotedCandidate:
    def __init__(self, persons, times):
        self.top_voted = []
        self.times = times

        p_cnt_map = collections.defaultdict(int)
        top_cnt, top_p = 0, None

        for p in persons:
            p_cnt_map[p] += 1
            if p_cnt_map[p] >= top_cnt:
                top_cnt = p_cnt_map[p]
                top_p = p
            self.top_voted.append(top_p)


    def q(self, t):
        idx = bisect.bisect_right(self.times, t) - 1
        return self.top_voted[idx]


class TopVotedCandidate:
    def __init__(self, persons, times):
        self.top_voted = []
        self.times = times

        p_cnt_map = collections.defaultdict(int)
        top_cnt, top_p = 0, None

        for p in persons:
            p_cnt_map[p] += 1
            if p_cnt_map[p] >= top_cnt:
                top_cnt = p_cnt_map[p]
                top_p = p
            self.top_voted.append(top_p)


    def q(self, t):
        idx = self.bisect_right(self.times, t) - 1
        return self.top_voted[idx]

    def bisect_right(self, times, t):
        lo, hi = 0, len(times)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if times[mid] <= t:
                lo = mid + 1
            else:
                hi = mid
        return lo

