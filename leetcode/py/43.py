'''
Input: num1 = "2", num2 = "3"
Output: "6"

Input: num1 = "123", num2 = "456"
Output: "56088"
       1 2 3
       4 5 6
    -----------
         1 8
       1 2
       6

       1 5
     1 0
     5

     1 2
     8
   4
-------------------

'''
class Solution:
    def multiply(self, num1, num2):
        res = [0] * (len(num1) + len(num2))

        for i, n1 in enumerate(num1[::-1]):
            for j, n2 in enumerate(num2[::-1]):
                res[i + j + 1], res[i + j] = divmod(int(n1) * int(n2) + res[i + j] + 10 * res[i + j + 1], 10)

        return ''.join(str(n) for n in res[::-1]).lstrip('0') or '0'