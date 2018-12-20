class Solution:
    def countCornerRectangles(self, grid):
        row_pair_cnt = collections.Counter()
        res = 0

        for row in grid:
            for r1, v1 in enumerate(row):
                if v1:
                    for r2 in range(r1 + 1, len(row)):
                        if row[r2]:
                            res += row_pair_cnt[(r1, r2)]
                            row_pair_cnt[(r1, r2)] += 1

        return res



class Solution:
    def countCornerRectangles(self, grid):
        rows = [[r for r, val in enumerate(row) if val] for row in grid]
        N = sum(len(row) for row in grid)
        SQRTN = int(N ** .5)

        res = 0
        count = collections.Counter()
        for r, row in enumerate(rows):
            if len(row) >= SQRTN:
                target = set(row)
                for r2, row2 in enumerate(rows):
                    if r2 <= r and len(row2) >= SQRTN:
                        continue
                    found = sum(1 for c2 in row2 if c2 in target)
                    res += found * (found - 1) / 2
            else:
                for pair in itertools.combinations(row, 2):
                    res += count[pair]
                    count[pair] += 1

        return res