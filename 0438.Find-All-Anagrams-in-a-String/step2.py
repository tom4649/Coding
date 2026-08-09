import collections


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_p = len(p)
        len_s = len(s)
        if len_p > len_s:
            return []

        count_p = collections.Counter(p)
        window = collections.Counter(s[:len_p])

        result: list[int] = []
        if window == count_p:
            result.append(0)

        for i in range(len_p, len_s):
            left, right = s[i - len_p], s[i]
            window[right] += 1
            window[left] -= 1
            if window[left] == 0:
                del window[left]
            if window == count_p:
                result.append(i - len_p + 1)

        return result


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_p = len(p)
        len_s = len(s)
        if len_p > len_s:
            return []

        def idx(c: str) -> int:
            return ord(c) - ord("a")

        count_p = [0] * 26
        for c in p:
            count_p[idx(c)] += 1

        window = [0] * 26
        for i in range(len_p):
            window[idx(s[i])] += 1

        result: list[int] = []
        if window == count_p:
            result.append(0)

        for i in range(len_p, len_s):
            window[idx(s[i])] += 1
            window[idx(s[i - len_p])] -= 1
            if window == count_p:
                result.append(i - len_p + 1)

        return result
