class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        transformed_s = "#" + "#".join(s) + "#"
        # radius[i]: index iを中心とする最長の回文半径
        radius = [0] * len(transformed_s)

        # すでに計算した回文半径を計算する
        def calculate_guaranteed_radius(center, rightmost_center, rightmost_right):
            # 過去の回文半径を利用できない場合
            if rightmost_right <= center:
                return 0

            # rightmost_center を中心にした反対側
            mirror = 2 * rightmost_center - center  # i - 2 * (i - center)

            # 最右の回文に中心mirrorの回文が覆われている場合: radius[mirror]
            # そうでない場合：rightmost_right - center
            # の半径は対称性より回文であることが保証される
            return min(rightmost_right - center, radius[mirror])

        # 過去に計算した半径を利用して回文半径を計算する
        def find_longest_on_center(center, guaranteed_radius):
            radius = guaranteed_radius
            left_candidate = center - radius - 1
            right_candidate = center + radius + 1
            while (
                0 <= left_candidate
                and right_candidate < len(transformed_s)
                and transformed_s[left_candidate] == transformed_s[right_candidate]
            ):
                radius += 1
                left_candidate -= 1
                right_candidate += 1

            return radius

        # これまで見つけた中で右端が最も遠い回文のもの
        rightmost_center = 0
        rightmost_right = 0

        # 最長の回文のもの
        longest_center = 0
        longest_radius = 0

        for center in range(len(transformed_s)):
            guaranteed_radius = calculate_guaranteed_radius(
                center, rightmost_center, rightmost_right
            )
            radius[center] = find_longest_on_center(center, guaranteed_radius)

            if center + radius[center] > rightmost_right:
                rightmost_center = center
                rightmost_right = center + radius[center]

            if radius[center] > longest_radius:
                longest_center = center
                longest_radius = radius[center]

        left_longest = (longest_center - longest_radius) // 2  # transformed_s -> sの変換
        return s[left_longest : left_longest + longest_radius]
