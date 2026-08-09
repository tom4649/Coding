# 236. Lowest Common Ancestor of a Binary Tree

## step1
pとqが見つかるまで木を探索し、見つかったら
以前"Lowest Common Ancestor of a Binary Search Tree"で書いた解法。

## 他の人のコード
https://github.com/huyfififi/coding-challenges/pull/46

かなりシンプルな解法になっている。自分の解法が冗長であったことを認識した。

左右に分岐する点を求める解法は計算量的に O(N^2)になってしまう(step2_top_down.py)。
この解法はtop-downであると言えるだろう。

> lowest common ancestorの解釈を少し変えているのでやや邪道な感じがするが、`p`と`q`が左右に分かれているパターンを判定するために、`q`を含まない`p`をrootとした部分木においても、`p`がlowest common ancestorだとしておく（`q`が部分木のrootの場合も同様に）。

この広義の定義と狭義の定義を区別した解法が「Cracking The Coding Interviewに載っていた」という解法であることも認識した。

この解法はbottom-upといえる(step2_bottom_up.py)。
時間計算量O(N)、空間計算量O(h)（最悪O(N)）

top-down、bottom-upという観点でいえば、step1の解法はハイブリッドと言える。
再帰を使っていない点では優れている。
