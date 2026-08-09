# 91. Decode Ways

## step1
DPで書いた。8mほど。配るDP。やや変数名を修正。

## step2
もらうDPで書いた。この場合は2変数で管理できる。

LeetCodeや他の方のSolutionを見ても新しいものはないので、LLMに聞いてみるとメモ化再帰を提案された。

トップダウンの解法

```python
from functools import cache

class Solution:
    def numDecodings(self, s: str) -> int:

        @cache
        def dfs(i: int) -> int:
            # 文字列の最後まで到達できたら、1つの有効な分割方法が見つかったということ
            if i == len(s):
                return 1
            # 0から始まるデコードは存在しない
            if s[i] == "0":
                return 0

            # パターン1: 1文字としてデコードする
            ans = dfs(i + 1)

            # パターン2: 2文字としてデコードする
            if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] <= "6")):
                ans += dfs(i + 2)

            return ans

        return dfs(0)
```
