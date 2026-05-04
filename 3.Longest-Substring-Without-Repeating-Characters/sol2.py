class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_index = {}
        start = 0
        max_length = 0
        for end, ch in enumerate(s):
            prev = last_index.get(ch, -1)
            if prev >= start:
                start = prev + 1
            last_index[ch] = end
            max_length = max(max_length, end - start + 1)
        return max_length
