# @param {String} s
# @return {Integer}
def length_of_longest_substring(s)
  set = Set.new
  start, max_len = 0, 0

  s.chars.each_with_index do |ch, idx|
    while set.include?(ch)
      set.delete(s[start])
      start += 1
    end
    set.add(ch)
    max_len = [idx - start + 1, max_len].max
  end

  return max_len
end




# map
def length_of_longest_substring(s)
  start, max_len = 0, 0
  hash = {}

  s.chars.each_with_index do |ch, idx|
    start = hash[ch] + 1 if hash.include?(ch) && hash[ch] >= start
    hash[ch] = idx
    max_len = [idx - start + 1, max_len].max
  end

  return max_len
end