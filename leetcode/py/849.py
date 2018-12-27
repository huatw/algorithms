'''
[1, 0, 0, 0, 1, 0, 1]
[0, 0, 0, 0, 4, 4, 6]
'''
class Solution:
    def maxDistToClosest(self, seats):
        left_dis = [-float('inf')]
        for i, seat in enumerate(seats):
            left_dis.append(i if seat else left_dis[-1])
        left_dis = left_dis[1:]

        right_dis = [float('inf')]
        for i, seat in reversed(list(enumerate(seats))):
            right_dis.append(i if seat else right_dis[-1])

        right_dis = right_dis[1:][::-1]
        return max(min(i - left, right - i) for i, (left, right) in enumerate(zip(left_dis, right_dis)))

