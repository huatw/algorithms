class Vector2D(object):
    def __init__(self, vec2d):
        self.vec2d = vec2d
        self.row_p = -1
        self.col_p = 0

    def next(self):
        return self.vec2d[self.col_p][self.row_p]

    def hasNext(self):
        if self.col_p >= len(self.vec2d):
            return False
        self.row_p += 1
        if self.row_p >= len(self.vec2d[self.col_p]):
            self.row_p = -1
            self.col_p += 1
            return self.hasNext()
        return True
