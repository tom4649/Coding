import List

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
        frontier = [(0, [])]

        while frontier:
            index_digit, fixed = frontier.pop()
            if index_digit == len(digits):
                result.append("".join(fixed))
                continue
            for c in DIGIT_TO_CHARS[digits[index_digit]]:
                frontier.append((index_digit + 1, fixed + [c]))

        return result
