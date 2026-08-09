class Solution:
    def compress(self, chars: list[str]) -> int:
        def append_count(length_before, count):
            length_after = length_before
            while count > 0:
                chars[length_after] = str(count % 10)
                count //= 10
                length_after += 1

            left = length_before
            right = length_after - 1
            while left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1

            return length_after

        length = 0
        index = 0

        while index < len(chars):
            c = chars[index]
            count = 0
            while index < len(chars) and chars[index] == c:
                index += 1
                count += 1
            chars[length] = c
            length += 1
            if count > 1:
                length = append_count(length, count)

        return length
