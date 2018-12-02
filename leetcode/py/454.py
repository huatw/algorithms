class Solution:
    def fourSumCount(self, A, B, C, D):
        ab_sum_map = collections.defaultdict(int)

        for a in A:
            for b in B:
                ab_sum_map[a + b] += 1

        return sum(ab_sum_map[-(c + d)] for c in C for d in D)



def fourSumCount(self, A, B, C, D):
    AB = collections.Counter(a + b for a in A for b in B)
    return sum(AB[-c-d] for c in C for d in D)