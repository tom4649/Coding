class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0

        num_end_with_i_minus_2 = 1  # 空文字列
        num_end_with_i_minus_1 = 1  # 最初の1文字

        for i in range(1, len(s)):
            num_end_with_i = 0

            if s[i] != "0":
                num_end_with_i += num_end_with_i_minus_1

            if s[i-1] != "0" and 10 <= int(s[i-1:i+1]) <= 26:
                num_end_with_i += num_end_with_i_minus_2

            if num_end_with_i == 0:
                return 0

            num_end_with_i_minus_2 = num_end_with_i_minus_1
            num_end_with_i_minus_1 = num_end_with_i

        return num_end_with_i_minus_1

