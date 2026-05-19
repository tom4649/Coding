class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def normalize(email):
            LOCAL, LOCAL_IGNORE, DOMAIN = 0, 1, 2
            out = []
            state = LOCAL
            for c in email:
                if state == LOCAL:
                    if c == ".":
                        continue
                    if c == "+":
                        state = LOCAL_IGNORE
                        continue
                    if c == "@":
                        state = DOMAIN
                        out.append("@")
                        continue
                    out.append(c)

                elif state == LOCAL_IGNORE:
                    if c == "@":
                        state = DOMAIN
                        out.append("@")
                else:
                    out.append(c)
            return "".join(out)

        return len({normalize(email) for email in emails})
