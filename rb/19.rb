# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val)
#         @val = val
#         @next = nil
#     end
# end

# @param {ListNode} head
# @param {Integer} n
# @return {ListNode}
def remove_nth_from_end(head, n)
  dummy = ListNode.new(nil)
  dummy.next = head

  fast, slow = dummy, dummy

  n.times { fast = fast.next }

  while fast.next
    fast = fast.next
    slow = slow.next
  end

  slow.next = slow.next.next

  return dummy.next
end