class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True

        def get_next(number):
            next_number = 0
            while number > 0:
                number, digit = divmod(number, 10)
                next_number += digit ** 2
            return next_number

        slow = n
        fast = get_next(n)
        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))

        return fast == 1
