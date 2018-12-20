class Solution:
    def customSortString(self, S, T):
        ch_ord_map = collections.defaultdict(int, {ch: i for i, ch in enumerate(S)})
        return sorted(T, key=lambda ch: ch_ord_map[ch])