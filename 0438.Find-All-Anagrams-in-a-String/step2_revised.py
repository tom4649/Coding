import collections


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_p = len(p)
        len_s = len(s)
        if len_p > len_s:
            return []

        histogram_in_p = collections.Counter(p)
        histogram_in_s = collections.Counter(s[:len_p])

        result: list[int] = []
        if histogram_in_s == histogram_in_p:
            result.append(0)

        for i in range(len_p, len_s):
            left, right = s[i - len_p], s[i]
            histogram_in_s[right] += 1
            histogram_in_s[left] -= 1
            if histogram_in_s[left] == 0:
                del histogram_in_s[left]
            if histogram_in_s == histogram_in_p:
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

        histogram_in_p = [0] * 26
        for c in p:
            histogram_in_p[idx(c)] += 1

        histogram_in_s = [0] * 26
        for i in range(len_p):
            histogram_in_s[idx(s[i])] += 1

        result: list[int] = []
        if histogram_in_s == histogram_in_p:
            result.append(0)

        for i in range(len_p, len_s):
            histogram_in_s[idx(s[i])] += 1
            histogram_in_s[idx(s[i - len_p])] -= 1
            if histogram_in_s == histogram_in_p:
                result.append(i - len_p + 1)

        return result
