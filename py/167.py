# two pointer
class Solution:
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers)-1

        while left < right:
            res = numbers[left] + numbers[right]
            if res == target:
                return [left+1, right+1]
            if res < target:
                left += 1
            else:
                right -= 1




# map
class Solution:
    def twoSum(self, numbers, target):
        map = {}
        for i, n in enumerate(numbers):
            if target - n in map:
                return [map[target-n]+1, i+1]
            map[n] = i



