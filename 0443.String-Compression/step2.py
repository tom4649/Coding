class Solution:
    def compress(self, chars: list[str]) -> int:
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
                for digit in str(count):
                    chars[length] = digit
                    length += 1

        return length
