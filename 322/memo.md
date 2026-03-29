# 322. Coin Change

そのまま思いついた方法として、メモ化再帰を実装: sol1.py
- 一発で通ったので気持ち良い

再帰関数を使わずに書く

- 動的計画法:

- 最短経路と考えればBFSで書ける
- tableを保持したsol3.pyを書いたが、coinをソートすれば早期breakができること、levelがそのまま答えになることに気づき、改良: sol4.py

## 計算量
amount = O(n), len(coins) = O(m)
### sol1.py
- 時間計算量 O(nm), 空間計算量 O(n) （=スタックフレーム、キャッシュ）
### sol2.py
- 時間計算量 O(nm), 空間計算量 O(n)
### sol4.py
- 時間計算量 O(nm), 空間計算量 O(n)


動的計画法
https://www.slideshare.net/slideshow/ss-3578511/3578511#1

自分のsol2.pyはもらうDP

https://github.com/TORUS0818/leetcode/pull/42#discussion_r1904039471
> -1 の扱いが気に入らなかったので Generator 使うのは考えてみました。

https://github.com/mamo3gr/arai60/blob/322_coin-change/322_coin-change/memo.md
> 再帰＋メモ化で、amount - coin でできる最小枚数をGeneratorで返させて、min(gen, default=-1) で最小値を取る。 自分もそれぞれ配列に入れてから min は思いついたが、最後に配列を舐めるのもなあ…と思って止めた。Generatorなら消費しながらminを取ってくれそう。

generatorなら作れない場合の無効値を流さず書くことができる（minを取るときにリストを作る必要もない）
minにdefaultがあることも知らなかった

