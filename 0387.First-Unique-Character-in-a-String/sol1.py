START_CHAR = "a"
START_CHAR_ORD = ord(START_CHAR)
NUM_CHARS = 26


class Solution:
    def firstUniqChar(self, s: str) -> int:
        ord_to_count = [0] * NUM_CHARS
        for c in s:
            ord_to_count[ord(c) - START_CHAR_ORD] += 1
        for i, c in enumerate(s):
            if ord_to_count[ord(c) - START_CHAR_ORD] == 1:
                return i
        return -1
