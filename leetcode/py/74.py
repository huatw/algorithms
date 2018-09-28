class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False

        lo, hi = 0, len(matrix) - 1

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if matrix[mid][0] > target:
                hi = mid - 1
            elif mid < len(matrix) - 1 and matrix[mid + 1][0] > target:
                lo = mid
                break
            else:
                lo = mid + 1

        row = matrix[lo]

        lo, hi = 0, len(row) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if row[mid] == target:
                return True
            if row[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1

        return False