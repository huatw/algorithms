class Solution:
    """
    @param nums: a list of integers
    @return: return an integer
    """
    def pathSum(self, nums):
        arr = [None] * 31
        cnts = [0, 1, 3, 7, 15]
        for num in nums:
            hundred = num // 100
            tenth = (num % 100) // 10
            val = num % 10
            arr[cnts[hundred - 1] + tenth - 1] = val

        res = 0
        stack = [(0, 0)]
        while stack:
            idx, acc = stack.pop()
            left_idx, right_idx = 2 * (idx + 1) - 1, 2 * (idx + 1)
            if arr[left_idx] == None and arr[right_idx] == None:
                res += acc + arr[idx]
            else:
                if arr[left_idx] != None:
                    stack.append((left_idx, acc + arr[idx]))
                if arr[right_idx] != None:
                    stack.append((right_idx, acc + arr[idx]))

        return res

