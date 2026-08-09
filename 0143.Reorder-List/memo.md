# 143. Reorder List

## step1
まずlistを使った方法を書いてみる。5mほど。これでは解けたことにならなそうなのでポインタのみを使って計算量を抑えたい。

Discussionの以下を見て解法を思いついた。後半を reverse すればいけそう。ヒントなしで解法には辿り着けなかった。

> Good practice for most of the important techniques of dealing with linked lists, ie. 2 pointer traversing, reversing, merging, ...

ここまで17mほど。変数名を改善

## 他の人のコード

https://github.com/thonda28/leetcode/pull/4

> ノード数が偶数のとき、真ん中のノードは、左半分の最後と右半分の最初の二つありますよね。どっちを返すかコメントに書いた方が分かりやすいです。

たしかに

- front, back, interleaveの命名

自分のformer, latterでもよいとは思った


> 最初からなるべく（ちょうどいい粒度の）関数に分けた方がいいのではないでしょうか？普段コードを書く時も、全てのコードをメイン関数に書いてから、関数化したりしないですよね。

関数化しようと思わなかったのは反省すべきなのかもしれない

https://github.com/potrue/leetcode/pull/68

## step2
## step3
