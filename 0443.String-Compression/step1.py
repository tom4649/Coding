class Solution:
    def compress(self, chars: list[str]) -> int:
        length = 0
        left = 0
        for right in range(len(chars) + 1):
            if right < len(chars) and chars[left] == chars[right]:
                continue
            chars[length] = chars[left]
            length += 1
            if right - left > 1:
                for c in str(right - left):
                    chars[length] = c
                    length += 1
            left = right

        return length
