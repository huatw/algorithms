class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()

        res = [set() for _ in range(target + 1)]
        res[0].add(())

        for can in candidates:
            for i in range(target, can-1, -1):
                if res[i - can]:
                    for t in res[i - can]:
                        res[i].add(t + (can,))

        return list(res[-1])




class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()

        res = []

        def dfs(remain, idx=0, path=[]):
            if remain == 0:
                res.append(path)
                return

            if remain > 0:
                for i in range(idx, len(candidates)):
                    c = candidates[i]

                    if i == idx or c != candidates[i-1]:
                        dfs(remain - c, i + 1, path + [c])

        dfs(target)

        return res





