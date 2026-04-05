class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1.0
        shifted = abs(n)
        current_pow = x
        while shifted > 0:
            if shifted & 1:
                result *= current_pow
            shifted >>= 1
            current_pow *= current_pow
        return result if n >= 0 else 1 / result
