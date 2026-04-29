# 141. Linked List Cycle
- [LeetCode: Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/description/)

- Set を使った実装
- 初回提出時に `set` に入れる値を `val` にしてしまい失敗
- `val` は重複しうるため、ノード（オブジェクト）そのものを `set` に入れることで成功
- 知識：`set` の平均/最悪計算量は \(O(1)\)/\(O(n)\)。最悪計算量はハッシュ衝突が起きたときに起こりうる
