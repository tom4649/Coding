MODULO = 10**9 + 7

class Solution:
    def checkRecord(self, n: int) -> int:
        A0_L0 = 1
        A0_L1 = 1
        A0_L2 = 0
        A1_L0 = 1
        A1_L1 = 0
        A1_L2 = 0

        for _ in range(n - 1):
            next_A0_L0 = (A0_L0 + A0_L1 + A0_L2) % MODULO
            next_A1_L0 = (A1_L0 + A1_L1 + A1_L2 + A0_L0 + A0_L1 + A0_L2) % MODULO
            next_A0_L1 = A0_L0 % MODULO
            next_A0_L2 = A0_L1 % MODULO
            next_A1_L1 = A1_L0 % MODULO
            next_A1_L2 = A1_L1 % MODULO

            A0_L0 = next_A0_L0
            A0_L1 = next_A0_L1
            A0_L2 = next_A0_L2
            A1_L0 = next_A1_L0
            A1_L1 = next_A1_L1
            A1_L2 = next_A1_L2

        return (A0_L0 + A0_L1 + A0_L2 + A1_L0 + A1_L1 + A1_L2) % MODULO
