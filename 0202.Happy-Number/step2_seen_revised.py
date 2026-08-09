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
                number, digit = divmod(number, 10)
                next_number += digit ** 2
            number = next_number

        return False
