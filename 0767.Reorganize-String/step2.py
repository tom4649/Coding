import collections


class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = collections.Counter(s)
        n = len(s)

        most_common_char, max_count = counter.most_common(1)[0]

        if max_count > (n + 1) // 2:
            return ""

        result = [""] * n
        index = 0

        for _ in range(max_count):
            result[index] = most_common_char
            index += 2

        del counter[most_common_char]

        for char, count in counter.items():
            for _ in range(count):
                if index >= n:
                    index = 1
                result[index] = char
                index += 2

        return "".join(result)
