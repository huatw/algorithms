class Solution:
    def numberOfBoomerangs(self, points):
        count = 0

        for x1, y1 in points:
            distances = collections.defaultdict(int)

            for x2, y2 in points:
                dis = (x1-x2) * (x1-x2) + (y1-y2) * (y1-y2)
                distances[dis] += 1

            nums += sum(n * (n-1) for n in distances.values())

        return count



