# 20. Valid Parentheses
- [リンク](https://leetcode.com/problems/valid-parentheses/description/)
- sol1を通したが書いているうちにスタックを思い出したので書き直し
- sol1は毎回文字列コピーが起こるのでO(n^2)
- sol2はO(n)
- collections.dequeを使った方が計算量が小さい
    - https://docs.python.org/3/library/collections.html#collections.deque
    - https://qiita.com/saba/items/107c4237206e31acdbef

### 解き直し
https://github.com/bumbuboon/Leetcode/pull/7#discussion_r1817837783
list の　空判定

https://github.com/bumbuboon/Leetcode/pull/7#discussion_r1817837783
スタックの底に番兵を置く

> 個人的には副作用のある式を条件のところにあまり書きたくない

https://github.com/yus-yus/leetcode/pull/6#discussion_r1944970090

