class Solution:
    def minWindow(self, S, T):
        dqs = [collections.deque([i for i, chs in enumerate(S) if cht == chs]) for cht in T]
        res = ''

        while dqs[0]:
            start = dqs[0].popleft()
            cur = start
            for dq in dqs[1:]:
                while dq and dq[0] <= cur:
                    dq.popleft()
                if not dq:
                    return res
                cur = dq[0]
            if not res or cur - start + 1 < len(res):
                res = S[start: cur + 1]

        return res
