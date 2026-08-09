class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        number = n

        while number not in seen:
            if number == 1:
                return True
            seen.add(number)
            next_number = 0
            while number > 0:
                next_number += (number % 10) ** 2
                number //= 10
            number = next_number

        return False
