# @param {Integer[]} nums
# @return {Integer[][]}
def three_sum(nums)
  nums.sort!

  res = []

  (nums.size - 2).times do |i|
    next if i != 0 && nums[i] == nums[i - 1]

    start_i, end_i = i + 1, nums.size - 1

    while start_i < end_i
      total = nums[start_i] + nums[end_i] + nums[i]

      res.push([nums[i], nums[start_i], nums[end_i]]) if total == 0

      if total <= 0
        start_i += 1
        start_i += 1 while nums[start_i] == nums[start_i - 1] && start_i < end_i
      end

      if total >= 0
        end_i -= 1
        end_i -= 1 while nums[end_i] == nums[end_i + 1] && start_i < end_i
      end
    end
  end

  return res
end