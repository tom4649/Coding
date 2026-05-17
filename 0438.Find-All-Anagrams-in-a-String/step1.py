import collections


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        char_to_count = collections.Counter(p)

        def validate_anagram(start: int) -> bool:
            char_to_count_copy = char_to_count.copy()
            for i in range(start, start + len(p)):
                char_to_count_copy[s[i]] -= 1
                if char_to_count_copy[s[i]] < 0:
                    return False
            return True

        result: list[int] = []
        start = 0
        while start < len(s) - len(p) + 1:
            if not validate_anagram(start):
                start += 1
                continue
            result.append(start)

            start += 1
            last = start + len(p) - 1
            while start < len(s) - len(p) + 1 and s[start - 1] == s[last]:
                result.append(start)
                start += 1
                last += 1

            while last < len(s) and s[last] != s[start - 1]:
                last += 1
            start = last - len(p) + 1

        return result
