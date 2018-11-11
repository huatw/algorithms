class Solution:
    def computeArea(self, x1, y1, x2, y2, x3, y3, x4, y4):
        area1 = (x2 - x1) * (y2 - y1)
        area2 = (x4 - x3) * (y4 - y3)
        width, height = min(x2, x4) - max(x1, x3), min(y2, y4) - max(y1, y3)
        overlap = width * height if width > 0 and height > 0 else 0
        return area1 + area2 - overlap
