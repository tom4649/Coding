# 124. Binary Tree Maximum Path Sum

## step1
再帰で書く。12mぐらい。

以下の点を間違えた
- 左右の子ノードを使う最大値を親ノードに返す（pathが分岐する）
- 関数を呼び出さずにmax_sumを返す

## 他の人のコード
https://github.com/shining-ai/leetcode/pull/69

考え方自体は同じだが書き方がやや異なる。

## step2
参考にして改善

