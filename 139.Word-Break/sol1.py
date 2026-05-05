import functools


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        len_target = len(s)

        @functools.cache
        def can_break(i) -> bool:
            if i == len_target:
                return True
            for word in wordDict:
                if s.startswith(word, i) and can_break(i + len(word)):
                    return True
            return False

        return can_break(0)
