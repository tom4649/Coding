# 300. Longest Increasing Subsequence
- sol1: 愚直な解法。素直に解くことができた
    - O(n**2)
- O(nlogn)の解法を思いつくことはできない
- https://github.com/mamo3gr/arai60/blob/300_longest-increasing-subsequence/300_longest-increasing-subsequence/memo.md
    - この方針だけ読んで考えたが無理
    - コードを読んでやっと理解

bisectの使い方

https://docs.python.org/3/library/bisect.html

```python
from bisect import bisect_left, bisect_right

a = [1, 3, 5]
print(bisect_left(a, 2))  # 1
print(bisect_left(a, 3))  # 1
print(bisect_right(a, 3))  # 2
```

https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0
> 日本語で長々と書くと、「lengths[i] とは、仮に nums[i] がシーケンスの最後であると仮定した場合に可能な、最も長いシーケンスの長さ」ですよね。
- 自分のsol1もlength_of_isなのでこの指摘が当てはまる

https://discord.com/channels/1084280443945353267/1200089668901937312/1209563502407065602

https://github.com/mamo3gr/arai60/blob/300_longest-increasing-subsequence/300_longest-increasing-subsequence/memo.md

- セグ木を使った解法、Binary Indexed Treeを使った解法
- 色々まとめてくれている

- セグメントツリー
    - https://github.com/naoto-iwase/leetcode/pull/36
- ほとんど写経で書いてみる
- 1-indexedにすることで、k%2==1: 右の子、k%2==0:左の子となる
- 座標圧縮を行う
- 自分より小さい数字であることを（座標圧縮した）indexで処理し、自分より前の数字であることをnumsの順番のループで処理
- 自力ではかけない

- BITを使った解法: LLMに書かせたが自分では書いていない。(sol4)
    - https://algo-logic.info/binary-indexed-tree/
    - 和の区間を最初からに限定することで、メモリと計算効率を上昇
    - bit演算で親や子への移動が可能
    - index & -index = lowbit[index]
    - これを足すことで親に移る
    - 自分では書けない

### 解き直し
O(nlog n)のsol2.pyは以前として思いつかなった
sol3.pyとsol4.pyをもう一度読んだ
セグツリーは見ないと書けないが使えるようにはなりたい
