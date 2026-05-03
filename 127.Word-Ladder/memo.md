# 127. Word Ladder
- dijkstraを使った(sol1.py)が、コストが1なのでbfsで十分だと気づいた
    - 時間計算量
    - はじめに隣接行列をつくるところでO(LN**2)
    - ヒープ部分でO((N+E)log N)
    - 空間計算量 O(E)
- 距離行列以外の場合にもグラフと見做せることを強く認識すべき
- https://github.com/mamo3gr/arai60/blob/127_word-ladder/127_word-ladder/memo.md
    - 丁寧に解いているので参考になる
    - subwordを利用すれば事前計算が O(LN) の時間計算量となるのはなるほど
    - デコレータclassmethodとstaticmethodの使い分け
    - bfsを使おうと思ったら愚直にキューを選択してしまいそうなので練習を兼ねてレベルbfsを書いてみる（sol2.py）
    - subwordの生成は理論的にはO(NL)だがスライス生成でO(NL**2)。組み込みを使っているので実際には高速だろう。
    - BFSの計算量は、最悪O(N**2L) (各単語subword L 個、to_visit N 個)
        - to_visitが分散してくれれば O(NL) より少し大きいぐらいか
    - 実際かなり速かった
- 双方向BFS
    - https://github.com/plushn/SWE-Arai60/pull/20/changes#r2588357494
    - 自力では書けそうにない
    - sol3.py
    - 常に小さい方から広げることで計算量を削減
    - 時間計算量 O(LN) (charの数を定数とみなす)
    - 空間計算量 O(N)


### 解き直し
BFSを用いた解法を思いついた: sol4_retry.py
しかし、前処理がO(N^2 L)になるので避けるべき解法であった
`subword`を使って`h*t -> hot, hit`のように1文字抜いた形から隣接候補を引けるようにすると、隣接判定のための全ペア比較を避けられる
もしくは各位置を`a-z`に置き換えて候補を作り、`set`に存在するかを見ると、文字種を定数とみなしてO(NL)寄りにできる

setのdiscardとremove
discard(x): x が存在すれば削除する。存在しなくても何も起きない。
remove(x): x が存在すれば削除する。存在しなければ KeyError になる。
