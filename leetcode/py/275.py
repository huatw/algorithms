class Solution:
    def hIndex(self, citations):
        N = len(citations)
        lo, hi = 0, N - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            # paper number which has more citations than citations[mid]
            if N - mid > citations[mid]:
                lo = mid + 1
            else:
                hi = mid - 1

        return N - lo
