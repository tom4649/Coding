import collections
import math


class WindowInfo:
    left = None
    right = None
    size = math.inf


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        required_count = collections.Counter(t)
        window_count = collections.defaultdict(int)
        num_required_unique_chars = len(required_count)
        num_formed_chars = 0

        window_info = WindowInfo()
        left = 0
        for right in range(len(s)):
            window_count[s[right]] += 1
            if window_count[s[right]] == required_count.get(s[right], -1):
                num_formed_chars += 1

            while num_formed_chars == num_required_unique_chars:
                if window_info.size > right - left + 1:
                    window_info.size = right - left + 1
                    window_info.left = left
                    window_info.right = right

                window_count[s[left]] -= 1
                if window_count[s[left]] < required_count.get(s[left], -1):
                    num_formed_chars -= 1
                left += 1

        if math.isinf(window_info.size):
            return ""
        return s[window_info.left : window_info.right + 1]
