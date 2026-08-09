import functools
class Solution:
    MODULO = 10 ** 9 + 7
    def countOrders(self, n: int) -> int:

        @functools.cache
        def count_orders_helper(n):
            if n == 1:
                return 1

            count = (self.countOrders(n - 1) * (2 * n - 1) * n) % self.MODULO
            return count

        return count_orders_helper(n)
