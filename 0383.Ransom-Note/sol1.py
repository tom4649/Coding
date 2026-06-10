from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        char_to_count_remaining = Counter(magazine)
        for c in ransomNote:
            if char_to_count_remaining.get(c, 0) == 0:
                return False
            char_to_count_remaining[c] -= 1
        return True
