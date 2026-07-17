class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]

        result = [0] * (n + 1)

        for i in range(n + 1):
            result[i] = i.bit_count()

        return result

