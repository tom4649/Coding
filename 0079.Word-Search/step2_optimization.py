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

        def traverse(
            row: int, col: int, letter_index: int, seen: list[list][bool]
        ) -> bool:
            if not word[letter_index] == board[row][col]:
                return False
            if letter_index == len(word) - 1:
                return True
            for row_next, col_next in (
                (row + 1, col),
                (row - 1, col),
                (row, col + 1),
                (row, col - 1),
            ):
                if (
                    0 <= row_next < num_row
                    and 0 <= col_next < num_col
                    and not seen[row_next][col_next]
                ):
                    seen[row_next][col_next] = True
                    if traverse(row_next, col_next, letter_index + 1, seen):
                        return True
                    seen[row_next][col_next] = False

            return False

        for row, col in itertools.product(range(num_row), range(num_col)):
            seen = [[False] * num_col for _ in range(num_row)]
            seen[row][col] = True
            if traverse(row, col, 0, seen):
                return True

        return False
