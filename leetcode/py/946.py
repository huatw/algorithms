'''
Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
1 2     3   4
    2 1   3   4
'''
# simulation
class Solution:
    def validateStackSequences(self, pushed, popped):
        stack = []
        j = 0

        for n in pushed:
            stack.append(n)
            while stack and j < len(popped) and popped[j] == stack[-1]:
                stack.pop()
                j += 1

        return j == len(popped)
