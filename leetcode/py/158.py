class Solution:
    # memo last status
    def __init__(self):
        self.last_buf = [None] * 4
        self.last_pointer = 0
        self.last_size = 0

    # left > n => n
    # left < n => n_left
    # 1. check last_buf, read4 if it is used
    # 2. check last_buf, break if nothing read
    # 3. last_buf -> buf
    # 4. reset pointer
    # 1. ->
    def read(self, buf, n):
        idx = 0
        while idx < n:
            # use last_buf if it exist
            if self.last_pointer == 0:
                self.last_size = Reader.read4(self.last_buf)
            # read4 empty
            if self.last_size == 0:
                break
            # last_buf write to buf
            while self.last_pointer < self.last_size and idx < n:
                buf[idx] = self.last_buf[self.last_pointer]
                self.last_pointer += 1
                idx += 1
            # reset pointer
            if self.last_pointer == self.last_size:
                self.last_pointer = 0
        return idx
