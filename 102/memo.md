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

- 再帰には深さに限界があるなど制約が多いので、ループに書き直せるようにしておく
    - https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.deivkzaqvetb
    - スタックをループに直すのは頻繁に必要になる。
    - 再帰だとログが難しい
    - spl2_loop.py:再帰+dfs
> 例えばですけれども、1万回くらい呼ぶと1回くらいおかしな動きをする機能があって、乱数などが絡んでいるから再現も難しいので、ある特定の if 文を通ったときにログを出力したいとします。再帰で書いていると、そもそもどういう状況でそこに到達したのかの関数の呼び出し元の情報などを出力するのが大変です。
- https://github.com/irohafternoon/LeetCode/pull/6#discussion_r2019026748

- Java デフォルトが 1M のスタックサイズ、C は 10M くらいが普通。
- Python setrecursionlimit: 言語処理系が設ける再帰上限
    - クラッシュ（Cスタック破壊）を避けるために、先に例外で止める
    - https://docs.python.org/3/library/sys.html#sys.getrecursionlimit
    - https://docs.python.org/3/library/sys.html#sys.setrecursionlimit
    - 言語処理形が上限を設ける
- クイックソートで長い方を末尾再帰最適化するのもスタックオーバーフローを防ぐため
    - https://nuc.hatenadiary.org/entry/2021/03/31#:~:text=%E7%9F%AD%E3%81%84%E6%96%B9%E3%81%8B%E3%82%89%E5%86%8D%E5%B8%B0%E3%81%97%E3%81%A6%E3%80%81%E9%95%B7%E3%81%84%E6%96%B9%E3%81%AF%E6%9C%AB%E5%B0%BE%E5%86%8D%E5%B8%B0%E6%9C%80%E9%81%A9%E5%8C%96%E3%81%99%E3%82%8B%E3%81%93%E3%81%A8



