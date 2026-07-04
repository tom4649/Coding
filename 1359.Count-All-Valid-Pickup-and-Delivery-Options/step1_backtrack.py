from enum import IntEnum

class OrderStatus(IntEnum):
    WAITING = 0
    PICKED_UP = 1
    DELIVERED = 2

class Solution:
    MODULO = 10 ** 9 + 7
    def countOrders(self, n: int) -> int:
        order_statuses = [OrderStatus.WAITING] * n
        count = 0

        def update_order_status(i):
            nonlocal count
            if i == 2 * n:
                count += 1
                count %= self.MODULO
                return

            for j in range(n):
                if order_statuses[j] == OrderStatus.DELIVERED:
                    continue

                if order_statuses[j] == OrderStatus.WAITING:
                    order_statuses[j] = OrderStatus.PICKED_UP
                    update_order_status(i + 1)
                    order_statuses[j] = OrderStatus.WAITING
                    continue

                order_statuses[j] = OrderStatus.DELIVERED
                update_order_status(i + 1)
                order_statuses[j] = OrderStatus.PICKED_UP

        update_order_status(0)
        return count
