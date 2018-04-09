# @param {Integer[]} height
# @return {Integer}
def max_area(height)
  left, right = 0, height.size - 1
  ret = 0

  while left < right
    area = (right - left) * [height[left], height[right]].min
    ret = area if area > ret

    if height[left] < height[right]
      left += 1
    else
      right -= 1
    end
  end

  return ret
end