# 56. Merge Intervals

## step1
25分ぐらいかかったが解けた。差分配列を用いた解法。

start == endのケースが面倒だった。

計算量
- 時間: O(n log n) ソートが支配的
- 空間: O(n)

## step2

### 他の人のコード

https://github.com/hayashi-ay/leetcode/pull/6#discussion_r1474516124

https://github.com/huyfififi/coding-challenges/pull/45

- 開始位置で区間をソートし、直前までマージ中の区間と今見ている区間を比較する
- `current_start <= merged_end` なら重なっているので、終端を `max(merged_end, current_end)` に更新する
- `merged_end < current_start` なら重なっていないので、マージ中の区間を結果に追加し、次の区間を新しいマージ対象にする

こちらの方が一般的だと思われる


