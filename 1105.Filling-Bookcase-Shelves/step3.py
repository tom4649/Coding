import functools

class Solution:
    def minHeightShelves(self, books: list[list[int]], shelfWidth: int) -> int:
        num_books = len(books)

        @functools.cache
        def min_height_from(i):
            if i == num_books:
                return 0

            total_width = 0
            max_height = 0
            min_total_height = float("inf")

            for j in range(i, num_books):
                width, height = books[j]
                total_width += width
                if total_width > shelfWidth:
                    break

                max_height = max(max_height, height)
                min_total_height = min(min_total_height, min_height_from(j + 1 ) + max_height)

            return min_total_height

        return min_height_from(0)

