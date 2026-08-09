import bisect

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        return (
            bisect.bisect_left(range(1, n + 1), True, key=lambda x: isBadVersion(x)) + 1
        )
