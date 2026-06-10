class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        char_count = [0] * 26
        for c in magazine:
            char_count[ord(c) - ord('a')] += 1
        for c in ransomNote:
            if char_count[ord(c) - ord('a')] == 0:
                return False
            char_count[ord(c) - ord('a')] -= 1
        return True
