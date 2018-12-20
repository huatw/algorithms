# binary search
class Solution:
    def splitArray(self, nums, k):
        def check(mid):
            cnt = 0
            cur_sum = 0
            for n in nums:
                if cur_sum + n > mid:
                    cur_sum = 0
                    cnt += 1
                    if cnt >= k:
                        return False
                cur_sum += n
            return True

        lo, hi = max(nums), sum(nums)

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo

# DP
# f[i][j] = max(f[k][j - 1], nums[k + 1] + ... + nums[i])
class Solution:
    def splitArray(self, nums, k):
        N = len(nums)
        dp = [[float('inf')] * (k + 1) for _ in range(N + 1)]
        acc = [0] + list(itertools.accumulate(nums))
        dp[0][0] = 0
        for i in range(1, N + 1): # 0 - i
            for j in range(1, k + 1): # j part
                for idx in range(i): # 0 - idx, j - 1 part; idx - i, 1 pary
                    dp[i][j] = min(dp[i][j], max(dp[idx][j - 1], acc[i] - acc[idx]))

        return dp[-1][-1]
