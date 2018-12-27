class Solution:
    def ipToInt(self, ip):
        res = 0
        for x in ip.split('.'):
            res = 256 * res + int(x)
        return res

    def intToIP(self, x):
        return ".".join(str((x >> i) % 256) for i in (24, 16, 8, 0))

    def ipToCIDR(self, ip, n):
        start = self.ipToInt(ip)
        res = []
        while n:
            mask = max(33 - (start & -start).bit_length(),
                       33 - n.bit_length())
            res.append(self.intToIP(start) + '/' + str(mask))
            start += 1 << (32 - mask)
            n -= 1 << (32 - mask)
        return res