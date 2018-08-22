class Solution:
    def medianSlidingWindow(self, nums, k):
        win = nums[:k - 1]
        win.sort()
        res = []
        is_odd = k % 2

        for i, n in enumerate(nums[k - 1:], k - 1):
            bisect.insort(win, nums[i])

            if is_odd:
                mid = win[k // 2]
            else:
                mid = (win[k // 2] + win[(k - 1) // 2]) / 2
            res.append(mid * 1.)

            head_n = bisect.bisect_left(win, nums[i - k + 1])
            win.pop(head_n)

        return res
