# 33. Search in Rotated Sorted Array

- 前二問（ソート+循環済み配列の最小値インデックス、単純なtarget探索）に分解できることに気づく
- 練習のためbisectを使わずに書いた
- 二分探索を一回で行う方法はあるのか？

https://discord.com/channels/1084280443945353267/1233295449985650688/1239594872697262121
- 二分探索を一回で行う方法を見つけた。賢すぎる。
- 関数 comp は target との大小で-1, 0, 1の三段階のスコアを振る。しかし循環されているので、これだと昇順にはならない。
- これを解消するためには、循環で本来の位置より前にきた数字のスコアを下げれば良い。最低どのくらい下げれば良いかというと、compの最大値と最小値との差 1-(-1) = 2である。この係数は-2以下であれば何でも良い。
- 自分でも空で書いてみる

https://github.com/hroc135/leetcode/pull/41#discussion_r1970984248
> 見直したら cmp いらなくて

なるほど、Pairにすれば解決するのか。自分で思いつきたかったな

https://github.com/mamo3gr/arai60/blob/33_search-in-rotated-sorted-array/33_search-in-rotated-sorted-array/memo.md



### 解き直し
Pair の方針で一発で解けたので嬉しい
