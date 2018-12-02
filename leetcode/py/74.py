# log(M) + log(N)
class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        M, N = len(matrix), len(matrix[0])

        lo, hi = 0, M - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if target > matrix[mid][-1]:
                lo = mid + 1
            elif target < matrix[mid][0]:
                hi = mid - 1
            else:
                lo = mid
                break

        row = matrix[lo]
        lo, hi = 0, N - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if target > row[mid]:
                lo = mid + 1
            else:
                hi = mid
        return row[lo] == target
