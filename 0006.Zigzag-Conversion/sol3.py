class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        zigzag = [[] for _ in range(numRows)]

        i = 0
        while i < len(s):
            for index_row in range(0, numRows - 1, 1):
                if i >= len(s):
                    break
                zigzag[index_row].append(s[i])
                i += 1
            for index_row in range(numRows - 1, 0, -1):
                if i >= len(s):
                    break
                zigzag[index_row].append(s[i])
                i += 1

        return "".join(c for row in zigzag for c in row)
