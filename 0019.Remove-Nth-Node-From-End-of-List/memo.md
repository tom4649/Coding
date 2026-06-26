# 19. Remove Nth Node From End of List

## step1
一巡して長さを求めて、もう一巡して削除を行う。8mぐらい。今回はミスがなかった。

削除したNodeのnextをNoneに変更した。メモリリークを明示的に防ぐためである。

制約も小さく、解くだけなら簡単な問題なので、他の方針も考える。

> Follow up: Could you do this in one pass?

hashmapを使えば実現できる

nth がendから数えたものなので、一度最後まで走査しないと削除が実行できない。これ以外の方針は思いつかない。

## 他の人のコード

https://github.com/thonda28/leetcode/pull/18

slowとfastを使うのか、なるほど。自分で思いつきたいところだった。

> step1のslow, fastの方が(個人的には)読みやすく感じました


このコードでは上述のメモリリークの対策はしていないようだが、した方が良いように思う

## step2

## pythonのメモリ管理について

https://daobook.github.io/devguide/garbage_collector.html

> The main garbage collection algorithm used by CPython is reference counting.

> ... it would never be cleaned just by simple reference counting. For this reason some additional machinery is needed to clean these reference cycles between objects once they become unreachable. This is the cyclic garbage collector, usually called just Garbage Collector (GC), ...

> Doubly linked lists are used because they efficiently support most frequently required operations. In general, the collection of all objects tracked by GC are partitioned into disjoint sets, each in its own doubly linked list.

- 主に参照カウント方式でgcが実装されている
- それだけでは防げない循環参照をcyclic garbage collectorで処理する
- 双方向リストによってオブジェクトの集合ごとに管理されている
- 循環参照の特定: 双方向連結リストにまとめる -> 身内同士の参照カウントをdecrement -> 参照が正のオブジェクトから辿れるオブジェクトをBFSし、参照カウント0のものは1にする -> 参照カウント0のオブジェクトを削除
- 再帰関数を使わない -> 省メモリ
- 世代別GC: 「新しく作られたオブジェクトのほとんどは、すぐに使われなくなる」仮説を利用する。世代の小さいものを優先的に削除する
