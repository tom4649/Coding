class Solution:
    def reverseBits(self, n: int) -> int:
        bit_expression = f"{n:032b}"
        return int(bit_expression[::-1], 2)

