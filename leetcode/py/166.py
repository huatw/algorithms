class Solution:
    def fractionToDecimal(self, numerator, denominator):
        sign = '' if numerator * denominator >= 0 else '-'
        numerator, denominator = abs(numerator), abs(denominator)

        n, remainder = divmod(numerator, denominator)
        res = [sign + str(n), '.']
        seen = {}
        idx = 2
        while remainder:
            seen[remainder] = idx
            idx += 1
            n, remainder = divmod(remainder * 10, denominator)
            res.append(str(n))
            if remainder in seen:
                res.insert(seen[remainder], '(')
                res.append(')')
                break
        return ''.join(res).rstrip('.')


