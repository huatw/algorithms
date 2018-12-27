import itertools

class Solution:
    def addBinary(self, a, b):
        res = []
        carry = 0

        for n1, n2 in itertools.zip_longest(a[::-1], b[::-1], fillvalue=0):
            carry, n = divmod(int(n1) + int(n2) + carry, 2)
            res.append(str(n))

        if carry:
            res.append(str(carry))

        return ''.join(res[::-1])