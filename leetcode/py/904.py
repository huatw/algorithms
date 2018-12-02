class Solution:
    def totalFruit(self, tree):
        lo = 0
        seen = collections.defaultdict(int)
        total = 0
        res = 0

        for hi, t in enumerate(tree):
            if seen[t] == 0:
                total += 1
            seen[t] += 1
            while total > 2:
                seen[tree[lo]] -= 1
                if seen[tree[lo]] == 0:
                    total -= 1
                lo += 1
            res = max(res, hi - lo + 1)

        return res