class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0

        dp = [0] * (len(s) + 1)
        dp[0] = 1

        for i in range(len(s)):
            if s[i] == "0":
                continue
            dp[i+1] += dp[i]
            if i + 1 < len(s) and int(s[i:i+2]) <= 26:
                dp[i+2] += dp[i]

        return dp[-1]


# solution = Solution()
# print(solution.numDecodings("12"))
# print(solution.numDecodings("226"))
# print(solution.numDecodings("0"))
# print(solution.numDecodings("1001"))
