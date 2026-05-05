class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False

        remaining_num_s = len(s)
        remaining_num_t = len(t)
        while remaining_num_s <= remaining_num_t:
            if s[len(s) - remaining_num_s] == t[len(t) - remaining_num_t]:
                remaining_num_s -= 1
            if remaining_num_s == 0:
                return True
            remaining_num_t -= 1

        return False
