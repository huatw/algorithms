class Solution:
    def fractionToDecimal(self, numerator, denominator):
        sign = '-' if numerator * denominator < 0 else ''
        numerator, denominator = abs(numerator), abs(denominator)
        n, remainder = divmod(numerator, denominator)
        res = [sign + str(n), '.']

        seen = {}
        count = 0
        while remainder != 0:
            seen[remainder] = count
            count += 1
            n, remainder = divmod(remainder * 10, denominator)
            res.append(str(n))
            if remainder in seen:
                res.insert(seen[remainder] + 2, '(')
                res.append(')')
                break
        return ''.join(res).rstrip('.')