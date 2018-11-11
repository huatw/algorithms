# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        buf4 = [''] * 4
        cnt = 0

        while n > 0:
            read_n = read4(buf4)
            if read_n == 0:
                break
            if n >= read_n:
                buf[cnt:cnt + read_n] = buf4[:read_n]
                cnt += read_n
                n -= read_n
            else:
                buf[cnt:cnt + n] = buf4[:n]
                cnt += n
                break
        return cnt



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
