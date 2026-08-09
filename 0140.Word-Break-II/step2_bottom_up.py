class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        word_set = set(wordDict)
        n = len(s)

        # dp[i]: s[i:]で作れる文字列のリスト
        dp = [[] for _ in range(n + 1)]
        dp[n] = [""]

        for i in range(n - 1, -1, -1):
            sentences = []
            for j in range(i + 1, n + 1):
                word = s[i:j]
                if word in word_set:
                    for sub in dp[j]:
                        if sub == "":
                            sentences.append(word)
                        else:
                            sentences.append(word + " " + sub)
            dp[i] = sentences

        return dp[0]
