class Solution:
    MODULO = 10 ** 9 + 7
    def countOrders(self, n: int) -> int:
        count = 1
        for i in range(n):
            num_order = i * 2
            num_insertion = (num_order + 1) * (num_order + 2) // 2 # 1 + 2 + ... (num_order + 1)
            count *= num_insertion % self.MODULO
            count %= self.MODULO

        return count
