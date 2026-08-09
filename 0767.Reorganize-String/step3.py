import collections


class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = collections.Counter(s)
        most_common_letter, most_common_count = counter.most_common()[0]

        if most_common_count > (len(s) + 1) // 2:
            return ""

        result = [""] * len(s)
        index = 0
        while most_common_count > 0:
            result[index] = most_common_letter
            index += 2
            most_common_count -= 1

        del counter[most_common_letter]

        for letter, count in counter.items():
            while count > 0:
                if index >= len(s):
                    index = 1
                result[index] = letter
                index += 2
                count -= 1

        return "".join(result)
