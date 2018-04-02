# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val)
#         @val = val
#         @next = nil
#     end
# end

# @param {ListNode} l1
# @param {ListNode} l2
# @return {ListNode}
def add_two_numbers(l1, l2)
  dummy = ListNode.new(nil)
  cur = dummy
  tenth = 0

  while l1 && l2
    tenth, digit = (l1.val + l2.val + tenth).divmod(10)
    cur.next = ListNode.new(digit)
    cur = cur.next
    l1 = l1.next
    l2 = l2.next
  end

  rest = l1 || l2
  while rest && !tenth.zero?
    tenth, digit = (rest.val + tenth).divmod(10)
    cur.next = ListNode.new(digit)
    cur = cur.next
    rest = rest.next
  end

  cur.next = tenth.zero? ? rest : ListNode.new(tenth)

  return dummy.next
end