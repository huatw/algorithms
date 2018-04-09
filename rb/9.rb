# @param {Integer} x
# @return {Boolean}
def is_palindrome(x)
  return false if x < 0
  return x.to_s.reverse.to_i == x
end




def is_palindrome(x)
  return true if x == 0
  return false if x < 0 || x % 10 == 0

  reflect = 0
  while reflect < x do
    x, remainder = x.divmod(10)
    reflect = 10 * reflect + remainder
  end

  reflect == x || (reflect / 10) == x
end