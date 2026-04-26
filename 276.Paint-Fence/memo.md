# 276 Paint Fence

https://www.lintcode.com/problem/514/

二状態のDPで解く: sol1.py
時間計算量 O(n)

メモ化再帰で書いても再帰で書くとテストケースに引っかかる。

### コメント集

https://github.com/goto-untrapped/Arai60/pull/44
フィボナッチ数列に似てるか

> フィボナッチ数列の極限は、黄金比の n 乗、になります。 (1 + sqrt(5)) / 2 これは、概ね、1.6 です。 (16/10)^n は、2^(4n) / 10^n で、log_2 10 ~ 0.301 を使うと、 ((1 + sqrt(5)) / 2)^n ~ 10^{(0.301*4-1)n} です。

log_2 10 -> log_{10} 2

https://github.com/shining-ai/leetcode/pull/30/changes#diff-a7a4b655731fbb220206ff9305969b66ac8cf7fd64bdcd12cbe6837749eac7bfR1-R9
DPの違う書き方もある


https://github.com/mamo3gr/arai60/blob/276_paint-fence/276_paint-fence/memo.md

https://github.com/naoto-iwase/leetcode/pull/35/changes#diff-c52fd179ae614e53682e0f0f57d5702672cbd03f0a4ef1c1e7b3c44f45e4f8fa

自分でLRU cacheを実装されている

doubly linked listとdictを組み合わせることで、挿入削除をO(1)で、キーからノードへの3勝もO(1)で実現している

公式の実装はスレッドセーフだったことを思い出す
https://docs.python.org/3/library/functools.html#functools.lru_cache

キーとしてタプルを用いるので、kwargsも含めるためには工夫が必要
辞書順でソートするなど




また、行列を利用して計算量をO(log n)にする工夫がある
