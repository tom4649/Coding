class Solution:
    def isHappy(self, n: int) -> bool:
        number = n

        while number != 1 and number != 4:
            next_number = 0
            while number > 0:
                number, digit = divmod(number, 10)
                next_number += digit ** 2
            number = next_number

        return number == 1
