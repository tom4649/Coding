# 1011. Capacity To Ship Packages Within D Days

https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/

TODO: 二分探索を自分で書く

- capacityを指定すればそれが可能かはO(N)で判定できる
- 上限をどのように定めるかが問題。単純にsum(weights)としたとき220ms、minを使ったとき119msとなった。
- 問題のWeight上限を使う方法は正攻法なのだろうか
- 自力で解法を思いついたが、二分探索のヒントがあったから

n = len(weights), M = maximum_valueとすると
- 時間計算量: O(n*log(M))
- 空間計算量: O(1) (入力は含めない)


コメント集に該当箇所はない

https://github.com/naoto-iwase/leetcode/pull/27/changes

capacityの下限はmax(weights)とできるのか
- これを反映してsol2.pyとしたが、149msとなり逆に遅くなった
- maxをとるO(n)の操作に余分な時間がかかるケースが多いのだろう。二分探索は途中で打ち切られるのでそれほど重くない。


https://github.com/mamo3gr/arai60/blob/1011_capacity-to-ship-packages-within-d-days/1011_capacity-to-ship-packages-within-d-days/memo.md

色々なコードがまとめられている

https://github.com/h1rosaka/arai60/pull/46/changes

上でも述べられているけど、 `for _ in range(days):` で書くこともできるのは思いつかなかった
