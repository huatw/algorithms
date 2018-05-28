# @param {Character[][]} board
# @param {String} word
# @return {Boolean}
def exist(board, word)
  board.each_with_index do |row, i|
    row.each_with_index do |item, j|
      return true if word[0] == item && search(i, j, board, word)
    end
  end

  # for i in 0...board.length
  #   for j in 0...board[i].length
  #       return true if search(i, j, board, word)
  #   end
  # end

  return false
end

def search(x, y, board, rest)
  return true if rest.empty?
  return false if x < 0 || y < 0 || x >= board.length || y >= board[0].length || board[x][y] != rest[0]

  temp = board[x][y]
  board[x][y] = nil

  ret = search(x - 1, y, board, rest[1..-1]) || search(x + 1, y, board, rest[1..-1]) || search(x, y - 1, board, rest[1..-1]) || search(x, y + 1, board, rest[1..-1])

  board[x][y] = temp
  return ret
end
