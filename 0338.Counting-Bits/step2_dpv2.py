class Solution:
    def countBits(self, n: int) -> list[int]:
        if n == 0:
            return [0]

        result = [0] * (n + 1)
        power_of_two = 1

        for i in range(1, n + 1):
            if i == power_of_two << 1:
                result[i] = 1
                power_of_two = i
            else:
                result[i] = result[i - power_of_two] + 1

        return result

