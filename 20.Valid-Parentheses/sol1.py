class Solution:
    def isValid(self, s: str) -> bool:
        bra_h_to_t = {
            "(": ")",
            "{": "}",
            "[": "]",
        }
        s_remained = s
        n_pos = 0
        while s_remained:
            if n_pos >= len(s_remained):
                return False
            while s_remained[n_pos] not in bra_h_to_t.values():
                n_pos += 1
                if n_pos >= len(s_remained):
                    return False
            if n_pos == 0 or s_remained[n_pos] != bra_h_to_t[s_remained[n_pos -1]]:
                return False
            s_remained = s_remained[:n_pos-1] + s_remained[n_pos+1:]
            n_pos -= 1
        return True








