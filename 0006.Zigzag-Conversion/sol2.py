class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        cycle_len = numRows * 2 - 2
        converted = []

        for i in range(0, len(s), cycle_len):
            converted.append(s[i])

        for row in range(1, numRows - 1):
            down_step = cycle_len - 2 * row
            up_step = 2 * row
            i = row
            while i < len(s):
                converted.append(s[i])
                i += down_step
                if i < len(s):
                    converted.append(s[i])
                    i += up_step

        for i in range(cycle_len // 2, len(s), cycle_len):
            converted.append(s[i])

        return "".join(converted)
