class Solution:
    def kSimilarity(self, A, B):
        def bfs(s):
            for i, (chs, cha) in enumerate(zip(s, B)):
                if chs != cha:
                    break
            res = []
            s = list(s)
            for j in range(i + 1, len(B)):
                if s[j] == B[i]:
                    s[i], s[j] = s[j], s[i]
                    res.append(''.join(s))
                    s[i], s[j] = s[j], s[i]
            return res

        seen = {A: 0}
        dq = collections.deque([A])

        while dq:
            s = dq.popleft()
            if s == B:
                return seen[s]
            for next_s in bfs(s):
                if next_s not in seen:
                    seen[next_s] = seen[s] + 1
                    dq.append(next_s)

