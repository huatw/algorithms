# @param {String} digits
# @return {String[]}
def letter_combinations(digits)
  map = {
    "2" => "abc",
    "3" => "def",
    "4" => "ghi",
    "5" => "jkl",
    "6" => "mno",
    "7" => "pqrs",
    "8" => "tuv",
    "9" => "wxyz"
  }

  return [] if digits == ""
  return map[digits[0]].chars if digits.size == 1

  map[digits[0]].chars.flat_map do |ch|
    letter_combinations(digits[1..-1]).map { |ch| ch + rest }
  end
end
