class Solution:
    def bagOfTokensScore(self, tokens, P):
        tokens = sorted(tokens)
        dq = collections.deque(tokens)

        res = 0
        points = 0

        while dq and (P >= dq[0] or points):
            while dq and P >= dq[0]:
                P -= dq.popleft()
                points += 1
            res = max(res, points)

            if dq and points:
                P += dq.pop()
                points -= 1

        return res