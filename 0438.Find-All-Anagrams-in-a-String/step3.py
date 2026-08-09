class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        def idx(c: str) -> int:
            return ord(c) - ord("a")

        count_p = [0] * 26
        window = [0] * 26
        for i in range(len(p)):
            count_p[idx(p[i])] += 1
            window[idx(s[i])] += 1

        anagram_starts = []
        for start in range(len(s) - len(p) + 1):
            if count_p == window:
                anagram_starts.append(start)

            if start < len(s) - len(p):
                start += 1
                window[idx(s[start - 1])] -= 1
                window[idx(s[start + len(p) - 1])] += 1

        return anagram_starts
