import re


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pattern = ""
        for c in s:
            pattern += ".*" + re.escape(c)
        return re.match(pattern, t) is not None
