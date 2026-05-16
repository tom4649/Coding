import collections


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        color_to_update = image[sr][sc]
        if color_to_update == color:
            return image

        frontier = collections.deque([(sr, sc)])

        while frontier:
            row, col = frontier.popleft()
            if not (0 <= row < len(image) and 0 <= col < len(image[0])):
                continue
            if image[row][col] != color_to_update:
                continue
            image[row][col] = color

            for next_row, next_col in (
                (row, col + 1),
                (row, col - 1),
                (row + 1, col),
                (row - 1, col),
            ):
                frontier.append((next_row, next_col))

        return image
