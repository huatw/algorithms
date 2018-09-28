# DP
class Solution:
    def canCross(self, stones):
        stone_map = {}

        for stone in stones:
            stone_map[stone] = set()

        stone_map[0].add(1)

        for stone in stones:
            for step in stone_map[stone]:
                # transform state to later stone
                if stone + step in stone_map:
                    for next_step in [step - 1, step, step + 1]:
                        if next_step > 0:
                            stone_map[stone + step].add(next_step)

        return len(stone_map[stones[-1]]) > 0