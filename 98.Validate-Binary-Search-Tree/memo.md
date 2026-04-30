# 98. Validate Binary Search Tree
[リンク](https://leetcode.com/problems/validate-binary-search-tree/submissions/1952536263/)

- 再帰 dfsで書いた: sol1_dfs_recursion.py
- 色々な解法: https://github.com/mamo3gr/arai60/blob/98_validate-binary-search-tree/98_validate-binary-search-tree/memo.md
- inorderに探索し、昇順になっているかを確認するのかでもとける
    - inorder + 再帰
    - https://github.com/nittoco/leetcode/pull/35/changes/BASE..cf57a354ba6d4fd06a3454283c3cec50011ce0c4#r1739978684
    - inorder + stackで書いてみる sol3

- 帰りがけ iterative
    - https://github.com/naoto-iwase/leetcode/pull/33#discussion_r2479195403
    - これは自分で書けそうにない
    - 親の left or rightに新しいノードが加えられる

- stack dfs
    - https://github.com/mamo3gr/arai60/blob/98_validate-binary-search-tree/98_validate-binary-search-tree/step3.py
    - 書いてみる： sol2

### 解き直し
変数名やコードの綺麗さを除けば、dfsはスラスラとかけた

inorderは書けなかった
- 常に自分より左のsubtreeが処理済みであることを仮定する
- BSTでは小さい値から走査していくことになる
