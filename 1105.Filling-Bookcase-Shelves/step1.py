from functools import cache

class Solution:
    def minHeightShelves(self, books: list[list[int]], shelfWidth: int) -> int:

        @cache
        def min_height_before(i):
            if i == len(books):
                return 0

            total_width = 0
            max_height = 0
            min_total_height = float("inf")
            for j in range(i, len(books)):
                width, height = books[j]
                total_width += width
                if total_width > shelfWidth:
                    break
                max_height = max(max_height, height)
                min_total_height = min(min_total_height, max_height + min_height_before(j + 1))

            return min_total_height

        return min_height_before(0)


