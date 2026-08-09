# 現れる文字が英数字であることを利用したカウント
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s = [0] * 26
        count_t = [0] * 26
        base = ord("a")
        for c in s:
            count_s[ord(c) - base] += 1
        for c in t:
            count_t[ord(c) - base] += 1
        return count_s == count_t


# 現れる文字が英数字であることを利用したカウントその2
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        cnt = [0] * 26
        base = ord("a")
        for i in range(len(s)):
            cnt[ord(s[i]) - base] += 1
            cnt[ord(t[i]) - base] -= 1
        return all(x == 0 for x in cnt)


# dictを利用したカウント
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_to_delta: dict[str, int] = {}
        for c in s:
            char_to_delta[c] = char_to_delta.get(c, 0) + 1
        for c in t:
            char_to_delta[c] = char_to_delta.get(c, 0) - 1
            if char_to_delta[c] < 0:
                return False
        return True


# Counterを利用
import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)
