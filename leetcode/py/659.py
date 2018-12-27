# O(n)
class Solution:
    def isPossible(self, nums):
        num_cnt_map = collections.Counter(nums)
        range_map = collections.defaultdict(int)

        for num in nums:
            if num_cnt_map[num] == 0:
                continue
            num_cnt_map[num] -= 1
            if range_map[num - 1] > 0:
                range_map[num - 1] -= 1
                range_map[num] += 1
            elif num_cnt_map[num + 1] > 0 and num_cnt_map[num + 2] > 0:
                num_cnt_map[num + 1] -= 1
                num_cnt_map[num + 2] -= 1
                range_map[num + 2] += 1
            else:
                return False
        return True

# O(N2)
class Solution:
    def isPossible(self, nums):
        stack = []

        for num in nums:
            found = False
            for arr in reversed(stack):
                if arr[-1] == num:
                    continue
                if arr[-1] + 1 == num:
                    arr.append(num)
                    found = True
                break
            if not found:
                stack.append([num])

        for arr in stack:
            if len(arr) < 3:
                return False
        return True