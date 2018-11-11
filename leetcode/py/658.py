'''
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]

Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]
'''
# O(n)
class Solution:
    def findClosestElements(self, arr, k, x):
        q = collections.deque()

        for num in arr:
            if len(q) == k:
                if abs(num - x) < abs(q[0] - x) or q[0] == num:
                    q.append(num)
                    q.popleft()
                else:
                    break
            else:
                q.append(num)

        return list(q)

# O(logn + k)
class Solution:
    def findClosestElements(self, arr, k, x):
        lo, hi = 0, len(arr) - k

        while lo < hi:
            start = lo + (hi - lo) // 2
            end = start + k - 1
            print(start, end, lo, hi)
            if arr[start] == arr[end]:
                if arr[start] < x:
                    lo = start + 1
                else:
                    hi = start - 1
            elif arr[end + 1] - x < x - arr[start]:
                lo = start + 1
            elif start - 1 >= 0 and x - arr[start - 1] <= arr[end] - x:
                hi = start - 1
            else:
                lo = start
                break

        return arr[lo:lo+k]


# find position first, then bisect
def findClosestElements(self, arr, k, x):
    left = right = bisect.bisect_left(arr, x)
    while right - left < k:
        if left == 0:
            return arr[:k]
        if right == len(arr):
            return arr[-k:]
        if arr[right] - x < x - arr[left - 1]:
            right += 1
        else:
            left -= 1
    return arr[left:right]
