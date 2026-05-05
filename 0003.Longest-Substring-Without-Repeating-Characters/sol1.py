class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        seen_char_to_idx = {}
        start = 0
        max_length = 0
        last = start + 1
        seen_char_to_idx[s[start]] = start
        while start < len(s):
            while last < len(s) and s[last] not in seen_char_to_idx:
                seen_char_to_idx[s[last]] = last
                last += 1
            max_length = max(max_length, last - start)
            if last >= len(s):
                break
            start = max(seen_char_to_idx[s[last]] + 1, start)
            seen_char_to_idx[s[last]] = last
            last += 1

        return max_length
