class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0

        num_ways = [0] * (len(s) + 1)
        num_ways[0] = 1

        for i in range(len(s)):
            if s[i] == "0":
                continue
            num_ways[i+1] += num_ways[i]
            if i + 1 < len(s) and int(s[i:i+2]) <= 26:
                num_ways[i+2] += num_ways[i]

        return num_ways[-1]


# solution = Solution()
# print(solution.numDecodings("12"))
# print(solution.numDecodings("226"))
# print(solution.numDecodings("0"))
# print(solution.numDecodings("1001"))
