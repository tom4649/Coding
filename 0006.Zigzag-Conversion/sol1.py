class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        num_one_group = numRows * 2 - 2
        converted = []
        for i in range(0, len(s), num_one_group):
            converted.append(s[i])
        for row_index in range(1, numRows - 1):
            i = row_index
            while True:
                if i >= len(s):
                    break
                converted.append(s[i])
                i += num_one_group - row_index * 2
                if i >= len(s):
                    break
                converted.append(s[i])
                i += row_index * 2
        for i in range(num_one_group // 2, len(s), num_one_group):
            converted.append(s[i])
        return "".join(converted)
