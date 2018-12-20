# (M+N)log(N)
class Solution:
    def findRadius(self, houses, heaters):
        heaters = sorted(heaters)

        res = 0
        for house in houses:
            if house <= heaters[0]:
                res = max(res, heaters[0] - house)
            elif house >= heaters[-1]:
                res = max(res, house - heaters[-1])
            else:
                idx = bisect.bisect(heaters, house)
                res = max(res, min(heaters[idx] - house, house - heaters[idx - 1]))
        return res

