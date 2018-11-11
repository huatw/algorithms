'''
Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
                      ^                                           ^
step1:  [b, l, u, e, "s","k","y"," ","i","s"," ", empty, t, h, e]
                                  ^           ^
                      i s empty      s k y
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]

[s k y]


in-place
'''
class Solution:
    def reverseWords(self, str):
