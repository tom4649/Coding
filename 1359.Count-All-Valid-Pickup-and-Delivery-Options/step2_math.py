import math

class Solution:
    MODULO = 10 ** 9 + 7
    def countOrders(self, n: int) -> int:
        numerator = math.factorial(2 * n) % self.MODULO
        denominator = pow(2, n, self.MODULO)
        return numerator * pow(denominator, -1, self.MODULO) % self.MODULO
