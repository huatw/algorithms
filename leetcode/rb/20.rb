# @param {String} s
# @return {Boolean}
def is_valid(s)
  hash = {
    ")"=> "(",
    "}"=> "{",
    "]"=> "["
  }

  stack = []

  for ch in (s.split '')
    if hash.key? ch
      return false if stack.pop != hash[ch]
    else
      stack.push ch
    end
  end

  stack.size == 0
end
