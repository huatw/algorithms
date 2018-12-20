# "XL" => "LX"  "RX" => "XR"
class Solution:
    def canTransform(self, start, end):
        for (i, x), (j, y) in itertools.zip_longest(
            ((i, x) for i, x in enumerate(start) if x != 'X'),
            ((j, y) for j, y in enumerate(end) if y != 'X'),
            fillvalue = (None, None)
        ):

            # If not solid or accessible, return False
            if x != y or (x == 'L' and i < j) or (x == 'R' and i > j):
                return False

        return True

class Solution:
    def canTransform(self, start, end):
        return all(x == y and ((x == 'L' and i >= j) or (x == 'R' and i <= j)) \
            for (i, x), (j, y) in itertools.zip_longest(
                ((i, x) for i, x in enumerate(start) if x != 'X'),
                ((j, y) for j, y in enumerate(end) if y != 'X'),
                fillvalue = (None, None)))