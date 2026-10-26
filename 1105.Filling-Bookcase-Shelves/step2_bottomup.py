class Solution:
    def minHeightShelves(self, books: list[list[int]], shelfWidth: int) -> int:
        num_books = len(books)

        min_height_from = [0] * (num_books + 1)

        for start_index in range(num_books - 1, -1, -1):

            shelf_width = 0
            shelf_height = 0
            min_total_height = float("inf")

            for end_index in range(start_index, num_books):
                width, height = books[end_index]

                shelf_width += width
                if shelf_width > shelfWidth:
                    break

                shelf_height = max(shelf_height, height)
                min_total_height = min(min_total_height, shelf_height + min_height_from[end_index + 1])

            min_height_from[start_index] = min_total_height

        return min_height_from[0]
