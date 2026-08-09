# 338. Counting Bits

## step1
4m ぐらい。hamming weightの問題の配列前計算の方法をまねた。計算量 O(n)。動的計画法である。

動的計画法を使わないと計算量は O(nlog n)になる。

しかし、実行速度自体は組み込み関数を使えばこの解法の方が速い。

Follow up もその旨が書かれている。

> It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?

## 他の人のコード
https://github.com/rihib/leetcode/pull/44

動的計画法だが考え方が異なる。自分のものは下一桁とそれ以外に分けていたが、これは上一桁とそれ以外に分けている。

> Rightmost set bitをunsetする方法
- x & (x - 1)
- x - (x & -x)

https://github.com/rihib/leetcode/blob/main/go/counting_bits.go
