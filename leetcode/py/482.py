class Solution:
    def licenseKeyFormatting(self, S, K):
        res = []
        cnt = 0

        for ch in reversed(S):
            if ch == '-':
                continue
            else:
                if cnt == 0 and res:
                    res.append('-')
                cnt += 1
                res.append(ch.upper())
                if cnt == K:
                    cnt = 0

        return ''.join(res[::-1])
