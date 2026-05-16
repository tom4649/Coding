class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        transformed = "#" + "#".join(s) + "#"
        # radius[i]: iを中心とする最長の回文半径
        radius = [0] * len(transformed)

        def calculate_guaranteed_radius(i, center, right):
            if right <= i:
                return 0

            mirror = 2 * center - i  # i + 2 * (center - i)
            return min(right - i, radius[mirror])

        def find_longest_on_center(i, guaranteed_radius):
            radius = guaranteed_radius
            left_candidate = i - radius - 1
            right_candidate = i + radius + 1
            while (
                0 <= left_candidate
                and right_candidate < len(transformed)
                and transformed[left_candidate] == transformed[right_candidate]
            ):
                radius += 1
                left_candidate -= 1
                right_candidate += 1
            return radius

        # これまで見つけた中で右端が最も遠い回文のもの
        center = 0
        right = 0

        longest_center = 0
        longest_radius = 0

        for i in range(len(transformed)):
            guaranteed_radius = calculate_guaranteed_radius(i, center, right)
            radius[i] = find_longest_on_center(i, guaranteed_radius)

            if i + radius[i] > right:
                center = i
                right = i + radius[i]

            if radius[i] > longest_radius:
                longest_center = i
                longest_radius = radius[i]

        start = (longest_center - longest_radius) // 2  # transformed -> sの変換で //2が必要
        return s[start : start + longest_radius]
