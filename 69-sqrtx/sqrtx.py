class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x < 2:
            return x
        
        n = 2
        while n * n <= x:
            n += 1
        
        return n - 1