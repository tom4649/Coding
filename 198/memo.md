# 198. House Robber

- 動的計画法を書いた


https://github.com/naoto-iwase/leetcode/pull/40
の実装2: without_lastとwith_lastの二変数だけで良い
- sol2.py

> このコードはスレッドセーフティーという意味でどうなっているでしょうか。

- cacheを使う場合（メモ化再帰）、キャッシュはthread safe: multi-threadで使用できる

https://github.com/hroc135/leetcode/pull/33#discussion_r1899009212
> フィボナッチになりそうですね。黄金比の n 乗なので 1.6^n くらいです
メモがない場合の計算量
https://ja.wikipedia.org/wiki/%E3%83%95%E3%82%A3%E3%83%9C%E3%83%8A%E3%83%83%E3%83%81%E6%95%B0


メモ化再帰も書いておく (sol3.py)
