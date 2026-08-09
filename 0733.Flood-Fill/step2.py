import collections


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        """BFS: 四方向はとりあえず全部キューに入れ、取り出したあと境界と元色を見る。"""
        base_color = image[sr][sc]
        if base_color == color:
            return image

        num_rows = len(image)
        num_cols = len(image[0])
        frontier = collections.deque([(sr, sc)])

        while frontier:
            row, col = frontier.popleft()
            if not (0 <= row < num_rows and 0 <= col < num_cols):
                continue
            if image[row][col] != base_color:
                continue
            image[row][col] = color
            frontier.append((row - 1, col))
            frontier.append((row + 1, col))
            frontier.append((row, col - 1))
            frontier.append((row, col + 1))

        return image


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        """BFS（deque）、キューに多重投入されても、取り出し時に base_color でないマスは skip。"""
        base_color = image[sr][sc]
        if base_color == color:
            return image

        num_rows = len(image)
        num_cols = len(image[0])
        directions = (
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
        )
        frontier = collections.deque([(sr, sc)])

        while frontier:
            row, col = frontier.popleft()
            if image[row][col] != base_color:
                continue
            image[row][col] = color
            for dr, dc in directions:
                row_next, col_next = row + dr, col + dc
                if (
                    0 <= row_next < num_rows
                    and 0 <= col_next < num_cols
                    and image[row_next][col_next] == base_color
                ):
                    frontier.append((row_next, col_next))

        return image


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        """DFS 再帰"""
        base_color = image[sr][sc]
        if base_color == color:
            return image

        num_rows = len(image)
        num_cols = len(image[0])

        def paint_region(row: int, col: int) -> None:
            if not (0 <= row < num_rows and 0 <= col < num_cols):
                return
            if image[row][col] != base_color:
                return
            image[row][col] = color
            for dr, dc in (
                (-1, 0),
                (1, 0),
                (0, -1),
                (0, 1),
            ):
                paint_region(row + dr, col + dc)

        paint_region(sr, sc)
        return image
