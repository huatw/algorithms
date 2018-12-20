class Solution:
    def nextGreaterElements(self, nums):
        res = []
        biggest = []

        for num in reversed(nums * 2):
            while biggest and biggest[-1] <= num:
                biggest.pop()
            res.append(biggest[-1] if biggest else -1)
            biggest.append(num)

        return res[len(nums):][::-1]


# map
class Solution:
    def nextGreaterElements(self, nums):
        n_map = {}
        stack = []

        for i, n in enumerate(nums):
            n_map[(n, i)] = -1
            while stack and stack[-1][0] < n:
                n_map[stack.pop()] = n
            stack.append((n, i))

        for n in nums:
            while stack and stack[-1][0] < n:
                n_map[stack.pop()] = n
            if not stack:
                break

        return [n_map[(n, i)] for i, n in enumerate(nums)]


# two pass
class Solution:
    def nextGreaterElements(self, nums):
        res = [-1] * len(nums)
        stack = []

        for i, n in reversed(list(enumerate(nums)) * 2):
            while stack and nums[stack[-1]] <= n:
                stack.pop()

            if stack:
                res[i] = nums[stack[-1]]

            stack.append(i)

        return res
