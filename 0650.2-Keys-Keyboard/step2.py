class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0

        steps = 0
        divisor = 2

        while divisor * divisor <= n:
            while n % divisor == 0:
                steps += divisor
                n //= divisor
            divisor += 1

        if n != 1:
            steps += n

        return steps
