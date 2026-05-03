import math


class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_to_idx = {}
        for i, c in enumerate(s):
            if c in char_to_idx:
                char_to_idx[c] = float("inf")
            else:
                char_to_idx[c] = i
        possible_answer = min(char_to_idx.values())
        return -1 if math.isinf(possible_answer) else possible_answer
