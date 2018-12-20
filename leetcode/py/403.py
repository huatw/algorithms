import functools

class Solution:
def canCross(self, stones):
        if len(stones) < 2:
            return True
        if stones[0] != 0 or stones[1] != 1:
            return False

        stone_set = set(stones)

        @functools.lru_cache(None)
        def dfs(pos, k):
            if pos not in stone_set:
                return False
            if pos == stones[-1]:
                return True
            return any(dfs(pos + next_k, next_k) for next_k in [k - 1, k, k + 1] if next_k > 0)

        return dfs(1, 1)

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
