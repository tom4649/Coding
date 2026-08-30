class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        if len(start) != len(result):
            return False
        if not start:
            return True

        index_start = 0
        index_result = 0

        while index_start < len(start) or index_result < len(result):
            while index_start < len(start) and start[index_start] == "X":
                index_start += 1
            while index_result < len(result) and result[index_result] == "X":
                index_result += 1

            if index_start == len(start) or index_result == len(result):
                return index_start == index_result

            if start[index_start] != result[index_result]:
                return False

            if start[index_start] == "L" and index_start < index_result:
                return False
            if start[index_start] == "R" and index_result < index_start:
                return False

            index_start += 1
            index_result += 1

        return True
