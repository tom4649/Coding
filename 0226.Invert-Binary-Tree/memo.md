# 226. Invert Binary Tree

## step1

再帰で書くとpost-orderのDFSが一番素直と思われる

## step2
post-orderを明示的に書く

pre-order, in-orderも書く

考え直すとpre-orderも自然。

ループでも書き直す。ループで書くならpre-orderが最も自然

{再帰, ループ} + {in-order, pre-order, post-order}の6通りできる。

### 他の人のコード

https://github.com/naoto-iwase/leetcode/pull/64

https://github.com/ryosuketc/leetcode_grind75/pull/6

https://github.com/Kitaken0107/GrindEasy/pull/9

https://github.com/Ryotaro25/leetcode_first60/pull/71

https://github.com/wf9a5m75/leetcode3/pull/13


BFSを書いていなかったので書く

tupleとlistどちらを使っても同じ場合はtupleを使うようにしているのだった。理由はオーバーヘッドが小さいから。

https://github.com/tom4649/Coding/pull/25/changes#diff-b335630551682c19a781afebcf4d07bf978fb1f8ac04c6bf87428ed5106870f5

で実験した。

ただし周囲のメンバーが違和感を感じる場合はそちらに合わせるのが良いだろう


