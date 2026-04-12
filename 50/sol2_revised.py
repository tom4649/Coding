class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n < 0:
            x = 1.0 / x
            n = -n
        sub_pow = self.myPow(x, n // 2)
        if n % 2 == 1:
            return sub_pow * sub_pow * x
        return sub_pow * sub_pow
