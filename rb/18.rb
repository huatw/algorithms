# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[][]}
def four_sum(nums, target)
  nums.sort!

  res = []

  nums[0...-3].each_with_index do |num, i|
    next if i > 0 && nums[i - 1] == num

    for j in i + 1...nums.size - 2
      num2 = nums[j]
      next if j > i + 1 && nums[j - 1] == num2

      left, right = j + 1, nums.size - 1
      while left < right
        total = num + num2 + nums[left] + nums[right]

        res.push([num, num2, nums[left], nums[right]]) if total == target
        if total <= target
          left += 1
          left += 1 while left < right && nums[left] == nums[left - 1]
        end

        if total >= target
          right -= 1
          right -= 1 while left < right && nums[right] == nums[right + 1]
        end
      end
    end
  end

  return res
end