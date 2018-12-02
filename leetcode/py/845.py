'''
Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
[2, 1, 4, 7, 3, 2, 5]
[0,0,1,0,0,1,1,1,1,1]
is_inc: True ->
is_inc: False ->
'''
class Solution:
    def longestMountain(self, A):
        res = 0
        lo = 0
        is_inc = None

        for hi, (prev_n, next_n) in enumerate(zip(A, A[1:])):
            if prev_n == next_n:
                if is_inc == False:
                    res = max(res, hi - lo + 1)
                is_inc = None
            elif is_inc:
                if next_n < prev_n:
                    is_inc = False
            else:
                if next_n > prev_n:
                    if is_inc == False:
                        res = max(res, hi - lo + 1)
                    is_inc = True
                    lo = hi

        if is_inc == False:
            res = max(res, len(A) - lo)

        return res