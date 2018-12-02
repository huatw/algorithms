'''
L1e2t1C1o1d1e1
'''
class StringIterator:
    def __init__(self, compressed):
        self.idx = -1
        self.compressed = compressed
        self.ch = None
        self.cnt = 0
        self.move_pointer()

    def move_pointer(self):
        if self.idx == len(self.compressed) - 1:
            return False
        self.idx += 1
        self.ch = self.compressed[self.idx]
        self.cnt = ''
        while self.idx + 1 < len(self.compressed) and self.compressed[self.idx + 1].isdigit():
            self.idx += 1
            self.cnt += self.compressed[self.idx]
        self.cnt = int(self.cnt)
        return True

    def next(self):
        if not self.hasNext():
            return ' '
        self.cnt -= 1
        res = self.ch
        if not self.hasNext():
            self.move_pointer()
        return res

    def hasNext(self):
        return self.cnt != 0