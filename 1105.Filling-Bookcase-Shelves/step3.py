import functools

class Solution:
    def minHeightShelves(self, books: list[list[int]], shelfWidth: int) -> int:
        num_books = len(books)

        @functools.cache
        def min_height_from(i):
            if i == num_books:
                return 0

            shelf_width = 0
            shelf_height = 0
            min_total_height = float("inf")

            for j in range(i, num_books):
                width, height = books[j]
                shelf_width += width
                if shelf_width > shelfWidth:
                    break

                shelf_height = max(shelf_height, height)
                min_total_height = min(min_total_height, min_height_from(j + 1 ) + shelf_height)

            return min_total_height

        return min_height_from(0)

