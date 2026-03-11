# 20. Valid Parentheses
- [リンク](https://leetcode.com/problems/valid-parentheses/description/)
- sol1を通したが書いているうちにスタックを思い出したので書き直し
- sol1は毎回文字列コピーが起こるのでO(n^2)
- sol2はO(n)
- collections.dequeを使った方が計算料が軽い
    - https://docs.python.org/3/library/collections.html#collections.deque
    - https://qiita.com/saba/items/107c4237206e31acdbef
