import re
from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        pattern = re.compile(r"^([a-z0-9.]+)(?:\+[^@]*)?@([a-z0-9.+]+)$")

        def normalize(email):
            match = pattern.fullmatch(email)
            if not match:
                raise ValueError
            local = match.group(1).replace(".", "")
            domain = match.group(2)
            return f"{local}@{domain}"

        return len({normalize(email) for email in emails})
