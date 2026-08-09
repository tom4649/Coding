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
        num_required_count = len(required_count)
        num_formed_count = 0
        window_info = WindowInfo()

        left = 0
        for right in range(len(s)):
            window_count[s[right]] += 1
            if window_count[s[right]] == required_count.get(s[right], -1):
                num_formed_count += 1

            while num_formed_count == num_required_count:
                if window_info.size > right - left + 1:
                    window_info.left = left
                    window_info.right = right
                    window_info.size = right - left + 1

                window_count[s[left]] -= 1
                if window_count[s[left]] < required_count.get(s[left], -1):
                    num_formed_count -= 1
                left += 1

        return (
            ""
            if math.isinf(window_info.size)
            else s[window_info.left : window_info.right + 1]
        )
