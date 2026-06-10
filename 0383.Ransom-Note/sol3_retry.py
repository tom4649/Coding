import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter_magazine = collections.Counter(magazine)

        for c in ransomNote:
            if counter_magazine.get(c, 0) == 0:
                return False
            counter_magazine[c] -= 1

        return True
