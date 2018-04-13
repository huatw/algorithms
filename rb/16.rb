# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def three_sum_closest(nums, target)
  nums.sort!

  min_diff = Float::INFINITY

  for i in 0...(nums.size - 2)
    next if i != 0 && nums[i] == nums[i - 1]

    left, right = i + 1, nums.size - 1
    while left < right
      diff = nums[i] + nums[left] + nums[right] - target
      return target if diff == 0

      min_diff = diff if diff.abs < min_diff.abs
      left += 1 if diff < 0
      right -= 1 if diff > 0
    end
  end

  return min_diff + target
end




def three_sum_closest(nums, target)
  nums.sort!

  min_diff = Float::INFINITY

  nums[0...-2].each_with_index do |v, i|
    next if i != 0 && v == nums[i - 1]

    left, right = i + 1, nums.size - 1
    while left < right
      diff = v + nums[left] + nums[right] - target
      return target if diff == 0

      min_diff = diff if diff.abs < min_diff.abs
      left += 1 if diff < 0
      right -= 1 if diff > 0
    end
  end

  return min_diff + target
end
