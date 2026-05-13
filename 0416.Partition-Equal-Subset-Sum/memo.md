# 416. Partition Equal Subset Sum

## step1
DP

和の最大値Mは 200 * 100 / 2 = 10^4 ほど

O(M^2)は許容されそう

25m ぐらいかかった

DP配列のコピーを作らないミス、細かいミスで時間を食った

## step2

意味もなくソートしていたのでやめた。DPテーブルのコメントもつけた。DP配列のコピーもやめた。


## 他の人のコード

https://github.com/huyfififi/coding-challenges/pull/51


- **指数探索の限界**: 各要素を使う／使わないで分岐する素朴な再帰は $2^n$ になり、制約（例: $n \le 200$）では TLE になりやすい。
- **`functools.cache` で `(subset_sum, index)` をメモ化**: TLE は避けられることがある一方、状態数が多く **MLE** に振れる例がある。方針としては DP 配列の方が筋がよい、という整理。
- **1 配列・逆順ループの意味**: 同じ `num` を同じ段で二度使わないため（0/1 ナップサック）。Discussion 等でよく説明されているパターン。
- **問題の見立て**: 「和が `sum(nums) // 2` になる部分集合があるか」は **Subset Sum（部分集合和）** の判定問題。Wikipedia の Subset sum problem にもあり、**0/1 ナップサック**の特別扱い、と整理できる。
- **ループの書き方の別形**: `sum` を `half_sum` から `num` まで降りながら `possible[sum] |= possible[sum - num]` とする C++ 実装（`step2.cpp`）。Python でいう「大きい方からの更新」と同値。
- **早期 return**: 内側ループの途中で `possible[half_sum]` が真になったら即 `true` を返す（`step4`）。最悪計算量は同じでも定数倍や平均が改善しうる。

早期 return を採用

## step 3
省略

