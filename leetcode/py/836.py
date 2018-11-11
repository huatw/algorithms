class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        def is_inside(x1, y1, x2, y2, x3, y3, x4, y4):
            return ((x1 <= x3 < x2) and (y1 <= y3 < y2)) \
                or ((x1 < x4 <= x2) and (y1 < y4 <= y2)) \
                or ((x1 <= x3 < x2) and (y1 < y4 <= y2)) \
                or ((x1 < x4 <= x2) and (y1 <= y3 < y2))

        def is_cross(x1, y1, x2, y2, x3, y3, x4, y4):
            return x1 < x3 < x4 < x2 and y3 < y1 < y2 < y4

        return is_inside(*rec1, *rec2) or is_inside(*rec2, *rec1) or is_cross(*rec1, *rec2) or is_cross(*rec2, *rec1)

class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2
        return not (x1 >= x4 or x2 <= x3 or y1 >= y4 or y2 <= y3)
