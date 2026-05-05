class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False
        index_s = 0
        for c in t:
            if s[index_s] == c:
                index_s += 1
                if index_s == len(s):
                    return True
        return False
