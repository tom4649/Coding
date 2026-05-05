class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        def generate_row_index():
            row_index = 0
            while True:
                while row_index < numRows - 1:
                    yield row_index
                    row_index += 1
                while row_index > 0:
                    yield row_index
                    row_index -= 1

        zigzag = [[] for _ in range(numRows)]
        for c, i in zip(s, generate_row_index()):
            zigzag[i].append(c)

        return "".join(c for row in zigzag for c in row)
