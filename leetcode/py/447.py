class Solution:
    def numberOfBoomerangs(self, points):
        total = 0

        for x, y in points:
            dis_cnt_map = collections.defaultdict(int)

            for x1, y1 in points:
                dis = (x - x1) ** 2 + (y - y1) ** 2
                dis_cnt_map[dis] += 1
            total += sum(cnt * (cnt - 1) for cnt in dis_cnt_map.values())

        return total

