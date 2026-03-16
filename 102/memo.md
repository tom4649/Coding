# 102. Binary Tree Level Order Traversal
[リンク](https://leetcode.com/problems/binary-tree-level-order-traversal/description/)

- sol1.py: 再帰でかいたがロジックがやや冗長かもしれない
    - DFSで帰りがけ順にマージする
    - 木が偏っている場合、時間計算量O(n**2)
    - 空間計算量 O(n)+O(h)

- https://github.com/mamo3gr/arai60/blob/102_binary-tree-level-order-traversal/102_binary-tree-level-order-traversal/step2.py
    - 行きがけ順の再帰
    - 似た感じで書く（sol2.py）
    - 時間計算量O(n**2)
    - 空間計算量 O(n)+O(h)

- https://discord.com/channels/1084280443945353267/1192728121644945439/1194203372115464272
    - if elseで例外処理を行うより、ifで例外だけを処理した方が良い
> 「機械の使い方の説明です。まず、青いランプが5つついていることを確認してください。ついている場合、…使い方の説明…。ランプがついていなかった場合は、直ちに使用を中止して事務所に連絡してください。…機械の使い方の続き…。」

- queueを使った BFS (sol4.py)
    - 時間計算量 O(n)
    - 空間計算量 O(n)
