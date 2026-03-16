class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def normalize_email(email: str) -> str:
            local, domain = email.split("@", 1)
            local = local.split("+", 1)[0].replace(".", "")
            return f"{local}@{domain}"

        return len({normalize_email(email) for email in emails})
