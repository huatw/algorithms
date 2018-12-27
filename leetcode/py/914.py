class Solution:
    def hasGroupsSizeX(self, deck):
        num_cnt_map = collections.Counter(deck)
        gcd = None

        for n in num_cnt_map.values():
            if not gcd:
                gcd = n
            else:
                gcd = math.gcd(gcd, n)

        return gcd >= 2