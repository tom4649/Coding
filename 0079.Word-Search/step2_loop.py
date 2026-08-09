import itertools
import collections


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        if not board or not board[0]:
            raise ValueError("invalid board")

        num_row = len(board)
        num_col = len(board[0])

        board_char_to_count = collections.Counter(itertools.chain.from_iterable(board))
        word_char_to_count = collections.Counter(word)

        for ch in word_char_to_count:
            if board_char_to_count[ch] < word_char_to_count[ch]:
                return False

        if board_char_to_count[word[-1]] < board_char_to_count[word[0]]:
            word = word[::-1]

        directions = (
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
        )

        def start_from(row_start: int, col_start: int) -> bool:
            if board[row_start][col_start] != word[0]:
                return False

            seen = [[False] * num_col for _ in range(num_row)]
            seen[row_start][col_start] = True
            stack = [(row_start, col_start, 0, 0)]

            while stack:
                row, col, letter_index, direction_index = stack[-1]
                if letter_index == len(word) - 1:
                    return True

                if direction_index == len(directions):
                    seen[row][col] = False
                    stack.pop()
                    continue

                d_row, d_col = directions[direction_index]
                stack[-1] = (row, col, letter_index, direction_index + 1)
                row_next = row + d_row
                col_next = col + d_col
                next_letter_index = letter_index + 1
                if (
                    0 <= row_next < num_row
                    and 0 <= col_next < num_col
                    and not seen[row_next][col_next]
                    and board[row_next][col_next] == word[next_letter_index]
                ):
                    seen[row_next][col_next] = True
                    stack.append((row_next, col_next, next_letter_index, 0))

            return False

        for row, col in itertools.product(range(num_row), range(num_col)):
            if start_from(row, col):
                return True

        return False
