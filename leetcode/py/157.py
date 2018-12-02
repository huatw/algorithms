

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):
class Solution(object):
    def read(self, buf, n):
        temp_buf = [''] * 4
        idx = 0
        while idx < n:
            temp_n = read4(temp_buf)
            if temp_n == 0:
                break
            temp_i = 0
            while idx < n and temp_i < temp_n:
                buf[idx] = temp_buf[temp_i]
                idx += 1
                temp_i += 1

        return idx



class Solution(object):
    def read(self, buf, n):
        buf4 = [""] * 4  # read4 buffer
        count = 0

        while n > 0:
            now = min(n, read4(buf4))
            if now == 0:  # no more to read
                break
            buf[count:count + now] = buf4[:now]  # copy from buf4 to buf
            count += now
            n -= now
        return count
