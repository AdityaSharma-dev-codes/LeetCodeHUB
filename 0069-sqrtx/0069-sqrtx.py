class Solution:
    def mySqrt(self, x: int) -> int:
        import math
        if x == 0:
            return 0
        i = 1
        while i*i < x:
            i += 1
        if i*i != x:
            i -= 1
        return math.floor(i)