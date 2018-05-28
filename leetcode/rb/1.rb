# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def two_sum(nums, target)
  hash = {}

  nums.each_with_index do |num, i|
    if hash.key? (target - num)
      break [hash[target - num], i]
    else
      hash[num] = i
    end
  end
end
