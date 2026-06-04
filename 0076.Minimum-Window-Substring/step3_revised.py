import collections


class WindowInfo:
    def __init__(self) -> None:
        self.left: int | None = None
        self.right: int | None = None
        self.size: int | None = None

    def update(self, left: int, right: int) -> None:
        self.left = left
        self.right = right
        self.size = right - left + 1


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        required_count = collections.Counter(t)
        window_count = collections.defaultdict(int)
        num_required_count = len(required_count)
        window_info = WindowInfo()

        left = 0
        for right in range(len(s)):
            window_count[s[right]] += 1
            if window_count[s[right]] == required_count.get(s[right], -1):
                num_required_count -= 1

            while num_required_count == 0:
                if window_info.size is None or window_info.size > right - left + 1:
                    window_info.update(left, right)

                window_count[s[left]] -= 1
                if window_count[s[left]] < required_count.get(s[left], -1):
                    num_required_count += 1
                left += 1

        return (
            ""
            if window_info.size is None
            else s[window_info.left : window_info.right + 1]
        )
