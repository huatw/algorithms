class Solution:
    def divide(self, dividend, divisor):
        # dividend / divisor
        def helper(dend,dsor):
            if dend < dsor:
                return 0
            cnt = 1
            acc = dsor
            while acc + acc < dend:
                acc += acc
                cnt += cnt
            return cnt + helper(dend - acc, dsor)

        op = 1 if (dividend < 0) == (divisor < 0) else -1
        res = op * helper(abs(dividend), abs(divisor))
        if res > 2 ** 31 - 1 or res < -2 ** 31:
            return 2 ** 31 - 1
        return res
