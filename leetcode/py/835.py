# N4
class Solution:
    def largestOverlap(self, A, B):
        diff_cnt_map = collections.Counter()

        for i, row in enumerate(A):
            for j, v in enumerate(row):
                if v:
                    for i2, row2 in enumerate(B):
                        for j2, v2 in enumerate(row2):
                            if v2:
                                diff_cnt_map[i - i2, j - j2] += 1

        return max(diff_cnt_map.values() or [0])


# N6
class Solution:
    def largestOverlap(self, A, B):
        A2 = [complex(r, c) for r, row in enumerate(A) for c, v in enumerate(row) if v]
        B2 = [complex(r, c) for r, row in enumerate(B) for c, v in enumerate(row) if v]
        b_set = set(B2)
        seen = set()
        res = 0

        for a in A2:
            for b in B2:
                d = b - a
                if d not in seen:
                    seen.add(d)
                    res = max(res, sum(x + d in b_set for x in A2))

        return res


