class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        base_color = image[sr][sc]
        seen = [[False] * len(image[0]) for _ in range(len(image))]
        stack = [(sr, sc)]
        seen[sr][sc] = True

        while stack:
            row, col = stack.pop()
            image[row][col] = color
            for row_next, col_next in (
                (row, col + 1),
                (row, col - 1),
                (row + 1, col),
                (row - 1, col),
            ):
                if not (0 <= row_next < len(image) and 0 <= col_next < len(image[0])):
                    continue
                if (
                    not seen[row_next][col_next]
                    and image[row_next][col_next] == base_color
                ):
                    stack.append((row_next, col_next))
                    seen[row_next][col_next] = True

        return image
