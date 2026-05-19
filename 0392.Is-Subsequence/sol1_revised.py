class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False

        index_s = 0
        for index_t in range(len(t)):
            if s[index_s] == t[index_t]:
                index_s += 1
                if index_s == len(s):
                    return True

        return False
