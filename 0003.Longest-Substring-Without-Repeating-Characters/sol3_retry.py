class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_to_last_index = {}
        start = -1
        max_length = 0
        for end, c in enumerate(s):
            prev = char_to_last_index.get(c, -1)
            if prev >= start:
                start = prev + 1
            max_length = max(max_length, end - start + 1)
            char_to_last_index[c] = end
        return max_length
