# ??
# DP
class Solution:
    def racecar(self, target):
        dp = [0, 1, 4] + [float('inf')] * target

        for t in range(3, target + 1):
            k = t.bit_length()
            if t == 2**k - 1:
                dp[t] = k
                continue
            for j in range(k - 1):
                dp[t] = min(dp[t], dp[t - 2**(k - 1) + 2**j] + k - 1 + j + 2)
            if 2**k - 1 - t < t:
                dp[t] = min(dp[t], dp[2**k - 1 - t] + k + 1)

        return dp[target]


# Dijkstra
class Solution:
    def racecar(self, target):
        K = target.bit_length() + 1
        barrier = 1 << K
        pq = [(0, target)]
        dist = [float('inf')] * (2 * barrier + 1)
        dist[target] = 0

        while pq:
            steps, targ = heapq.heappop(pq)
            if dist[targ] > steps:
                continue

            for k in range(K+1):
                walk = (1 << k) - 1
                steps2, targ2 = steps + k + 1, walk - targ
                if walk == targ:
                    steps2 -= 1 #No "R" command if already exact

                if abs(targ2) <= barrier and steps2 < dist[targ2]:
                    heapq.heappush(pq, (steps2, targ2))
                    dist[targ2] = steps2

        return dist[0]


# BFS
class Solution:
    def racecar(self, target):
        seen = set([(0, 1)])
        level = [(0, 1)]
        steps = 0
        while level:
            steps += 1
            next_level = []
            for (pos, speed) in level:
                for next_pair in [(pos + speed, speed * 2), (pos, -1 if speed > 0 else 1)]:
                    if next_pair in seen or (pos > target and next_pair[1] > 0):
                        continue
                    if next_pair[0] == target:
                        return steps
                    seen.add(next_pair)
                    next_level.append(next_pair)
            level = next_level

