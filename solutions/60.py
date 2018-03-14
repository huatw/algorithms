class Solution:
    def getPermutation(self, n, k):
        res, nums = "",  list(map(str, range(1, n+1)))
        k -= 1

        while n:
            n -= 1
            index, k = divmod(k, math.factorial(n))
            res += nums.pop(index)

        return res