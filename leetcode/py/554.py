class Solution:
    def leastBricks(self, wall):
        width_cnt_map = collections.defaultdict(int)

        for level in wall:
            total = 0
            for n in level:
                total += n
                width_cnt_map[total] += 1
        width_cnt_map[total] = 0

        return len(wall) - max([cnt for cnt in width_cnt_map.values()])
