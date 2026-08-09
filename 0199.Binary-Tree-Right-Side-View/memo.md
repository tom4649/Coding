# 199. Binary Tree Right Side View

## step1

右の子を先に処理するin-orderで書ける。8mぐらい。

nonlocal をつけずに一度間違えた。変数のスコープを意識できていないためなので反省。

Mediumの問題の中ではスラスラと解けた方だと思う。

## step2
pre-order, bfsでも書ける。nonlocalな変数が不要になる。MAX_NODESも不要になるのでこちらが良さそう。

その他、これ以降これ以降以下のように型を意識していきたい。
- List[] -> list[]と書き直す
- 空のコンテナには型をつける
- 関数にも型をつける


### 他の人のコード
https://github.com/huyfififi/coding-challenges/pull/55

上書きするようにすれば左を先に処理するpre-order, bfsでも書ける。




