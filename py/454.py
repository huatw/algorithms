# hashmap O(n2)
class Solution:
    def fourSumCount(self, A, B, C, D):
        res = 0
        m = set()

        for na in A:
            for nb in B:
                m.add(-(na + nb))

        for nc in C:
            for nd in D:
                if nc + nd in m:
                    res += 1

        return res


def fourSumCount(self, A, B, C, D):
    AB = collections.Counter(a + b for a in A for b in B)
    return sum(AB[-c-d] for c in C for d in D)