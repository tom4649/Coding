from typing import List


DIGIT_TO_CHARS = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        result = []

        def generate_combinations_from(index, fixed):
            if index == len(digits):
                result.append("".join(fixed))
                return
            for c in DIGIT_TO_CHARS[digits[index]]:
                fixed.append(c)
                generate_combinations_from(index + 1, fixed)
                fixed.pop()

        generate_combinations_from(0, [])
        return result
