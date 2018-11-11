class Solution:
    def sortColors(self, nums):
        color_map = {
            0: 0,
            1: 0,
            2: 0
        }

        for num in nums:
            color_map[num] += 1

        for cnt, (lo, hi) in enumerate([(0, color_map[0]), (color_map[0], color_map[0] + color_map[1]), (color_map[0] + color_map[1], len(nums))]):
            for i in range(lo, hi):
                nums[i] = cnt

class Solution:
    def sortColors(self, nums):
        red, white, blue = 0, 0, len(nums)-1

        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                red += 1
                white += 1
            elif nums[white] == 2:
                nums[blue], nums[white] = nums[white], nums[blue]
                blue -= 1
            else:
                white += 1


