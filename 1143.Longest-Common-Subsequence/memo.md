# 1143. Longest Common Subsequence

## step1

動的計画法の練習として解く。

動的計画法を使うという事前知識のもとで解けた。

動的計画法を使うという知識がないときに解けないのが問題なのだが。

## 解法

https://leetcode.com/problems/longest-common-subsequence/solutions/436719/python-very-detailed-solution-with-expla-gxr8/

Unixのdiffコマンドで使われる。

以下のメモ化再帰からDPという流れで解説している。

```python
class Solution:
        def longestCommonSubsequence(self, s1: str, s2: str) -> int:
            m = len(s1)
            n = len(s2)
            memo = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
            return self.helper(s1, s2, 0, 0, memo)

        def helper(self, s1, s2, i, j, memo):
            if memo[i][j] < 0:
                if i == len(s1) or j == len(s2):
                    memo[i][j] = 0
                elif s1[i] == s2[j]:
                    memo[i][j] = 1 + self.helper(s1, s2, i + 1, j + 1, memo)
                else:
                    memo[i][j] = max(
                        self.helper(s1, s2, i + 1, j, memo),
                        self.helper(s1, s2, i, j + 1, memo),
                    )
            return memo[i][j]
```

さらに空間計算量を減らすための工夫。必要なセルが前の二行だけであることを利用する。

```python
class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)
        if m < n:
            return self.longestCommonSubsequence(s2, s1)
        memo = [[0 for _ in range(n + 1)] for _ in range(2)]

        for i in range(m):
            for j in range(n):
                if s1[i] == s2[j]:
                    memo[1 - i % 2][j + 1] = 1 + memo[i % 2][j]
                else:
                    memo[1 - i % 2][j + 1] = max(memo[1 - i % 2][j], memo[i % 2][j + 1])

        return memo[m % 2][n]
```

### step2, step3
動的計画法の練習のために解いたので省略。
