class Solution:
    def getFactors(self, n):
        ret, stack, x = [], [], 2
        while True:
            if x > n / x:
                if not stack:
                    return ret
                ret.append(stack + [n])
                x = stack.pop()
                n *= x
                x += 1
            elif n % x == 0:
                stack.append(x)
                n /= x
            else:
                x += 1