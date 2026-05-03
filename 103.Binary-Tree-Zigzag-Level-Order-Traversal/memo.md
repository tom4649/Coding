# 103. Binary Tree Zigzag Level Order Traversal
- [リンク](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/)
- https://github.com/mamo3gr/arai60/blob/103_binary-tree-zigzag-level-order-traversal/103_binary-tree-zigzag-level-order-traversal/memo.md
- リストを「逆順」に扱う方法（用途で選ぶ）
    - `xs.reverse()`：破壊的（in-place）。リスト自体を反転して良いなら最有力
    - `reversed(xs)`：非破壊の逆順イテレータ。`for` で回すだけならこれが軽い（コピー不要）
    - `list(reversed(xs))` / `xs[::-1]`：**非破壊**で「反転した新しいリスト」が欲しいとき（どちらも \(O(n)\) コピー）
    - 手動で `for i in range(len(xs)-1, -1, -1)`：特殊な制御が必要なときだけ（可読性は落ちがち）
- 勉強のためにdfs+再帰も書く

### 解き直し
BFSで書いた気がするのだが、なくなっていたのでもう一度書く。
レビューで指摘されたようにこちらが自然な気がする。
