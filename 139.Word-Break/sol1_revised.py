import functools


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        len_target = len(s)

        @functools.cache
        def can_break(start_pos: int) -> bool:
            """returns whether s[start_pos:] can be broken."""
            if start_pos == len_target:
                return True
            for word in wordDict:
                if s.startswith(word, start_pos) and can_break(start_pos + len(word)):
                    return True
            return False

        return can_break(0)
