# DP
class Solution:
    def canCross(self, stones):
        if len(stones) < 2:
            return True

        if stones[0] != 0 and stones[1] != 1:
            return False

        stone_map = {stone: set() for stone in stones}
        stone_map[0].add(1)

        for stone in stones:
            for step in stone_map[stone]:
                # transform state to later stone
                if stone + step == stones[-1]:
                    return True
                if stone + step in stone_map:
                    for next_step in [step - 1, step, step + 1]:
                        if next_step > 0:
                            stone_map[stone + step].add(next_step)

        return False
