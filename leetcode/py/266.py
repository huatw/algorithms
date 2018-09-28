def palindrome(s):
     ch_set = set()

     for ch in s:
          if ch in ch_set:
               ch_set.remove(ch)
          else:
               ch_set.add(ch)

     return len(ch_set) <= 1
