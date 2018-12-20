'''
0 1 2 3 ..w         k .. n
1 1 1 1 ..1 0 0 ... 0 .. 0
    2 2 ..2 1
      3 ..3 2 1
          4 3 2 1...

          w...........1
              k .. n

<= N
[K, K + W)
'''
class Solution:
    def new21Game(self, N, K, W):
        if K == 0 or N >= K + W:
            return 1
        dp = [1.0] + [0.0] * N
        w_sum = 1.0
        for i in range(1, N + 1):
            dp[i] = w_sum / W
            if i < K: # add prob, since we do not stop at i < K
                w_sum += dp[i]
            if i - W >= 0: # drop prob
                w_sum -= dp[i - W]
        return sum(dp[K:])




class Solution:
    def new21Game(self, N, K, W):
        if K == 0 or N >= K + W:
            return 1

        dp = [1]
        w_sum = 1
        for i in range(N):
            prob = w_sum / W
            dp.append(prob)
            if i < K - 1:
                w_sum += prob
            if i >= W - 1:
                w_sum -= dp[i - W + 1]

        return sum(dp[K:])
