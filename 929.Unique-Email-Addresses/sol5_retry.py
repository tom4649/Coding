from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def normalize(s):
            local, split, domain = s.partition("@")
            if split != "@":
                raise ValueError("Invalid Email")
            local_used, _, _ = local.partition("+")
            local_used_without_dots = local_used.replace(".", "")
            return f"{local_used_without_dots}@{domain}"

        return len({normalize(email) for email in emails})
