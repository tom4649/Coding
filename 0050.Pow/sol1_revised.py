class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1.0
        exponent = abs(n)
        current_pow = x
        while exponent > 0:
            if exponent & 1:
                result *= current_pow
            exponent >>= 1
            current_pow *= current_pow
        return result if n >= 0 else 1 / result
