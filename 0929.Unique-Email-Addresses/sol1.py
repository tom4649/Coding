class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def normalize_email(email):
            idx_at = None
            idx_plus = None
            idxs_dot = []
            for i, c in enumerate(email[::-1]):
                if c == "@":
                    idx_at = len(email) - i - 1
                if idx_at is not None and c == "+":
                    idx_plus = len(email) - i - 1
                if idx_at is not None and c == ".":
                    idxs_dot.append(len(email) - i - 1)
            if idx_at is None:
                raise ValueError
            normalized_email = email
            if idx_plus is not None:
                normalized_email = (
                    normalized_email[:idx_plus] + normalized_email[idx_at:]
                )
            for idx_dot in idxs_dot:
                if idx_plus is not None and idx_plus < idx_dot:
                    continue
                normalized_email = (
                    normalized_email[:idx_dot] + normalized_email[idx_dot + 1 :]
                )
            return normalized_email

        unique_emails = set()
        for email in emails:
            unique_emails.add(normalize_email(email))
        return len(unique_emails)
