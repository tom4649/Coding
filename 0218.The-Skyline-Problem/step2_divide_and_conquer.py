class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        if not buildings:
            return []

        def merge(left_skyline, right_skyline):
            left_index = 0
            right_index = 0
            left_height = 0
            right_height = 0
            x = 0
            merged = []

            while left_index < len(left_skyline) or right_index < len(right_skyline):
                if right_index == len(right_skyline) or (left_index < len(left_skyline) and left_skyline[left_index][0] < right_skyline[right_index][0]):
                    x = left_skyline[left_index][0]
                    left_height = left_skyline[left_index][1]
                    left_index += 1
                elif left_index == len(left_skyline) or (right_index < len(right_skyline) and right_skyline[right_index][0] < left_skyline[left_index][0]):
                    x = right_skyline[right_index][0]
                    right_height = right_skyline[right_index][1]
                    right_index += 1
                else:
                    x = left_skyline[left_index][0]
                    left_height = left_skyline[left_index][1]
                    right_height = right_skyline[right_index][1]
                    left_index += 1
                    right_index += 1

                height = max((left_height, right_height))
                if not merged or merged[-1][1] != height:
                    merged.append([x, height])

            return merged

        def get_skyline_helper(start, last):
            if start == last:
                left, right, height = buildings[start]
                return [[left, height], [right, 0]]

            middle = (start + last) // 2
            left_skyline = get_skyline_helper(start, middle)
            right_skyline = get_skyline_helper(middle + 1, last)

            return merge(left_skyline, right_skyline)

        return get_skyline_helper(0, len(buildings) - 1)
