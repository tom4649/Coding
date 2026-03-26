
# 105. Construct Binary Tree from Preorder and Inorder Traversal

- sol1: 愚直な方針。再帰でpreorderの先頭が根であり、preorderでその位置を特定して再帰。
    - 時間計算量: 根の探索とスライス作成で最悪O(n**2)
    - 空間計算量: スライス作成で最悪O(n**2)
    - 再帰スタック：O(h), 最悪O(n)
    - 時間の具体的な見積もり：n = 3000, Python 10^7として　 3000 **2 / 10^7 = 0.9s
- sol2: 再帰は変えずに、inorder の値→index の辞書を作って (O(1)) で位置を引き、再帰は「配列の範囲（左右境界）」で表す（スライスしない）。
    - 時間計算量: 最初の val_to_indexの計算でO(n)
    - 空間計算量: val_to_indexのみなのでO(n)
    - 再帰スタックは上と同じ
    - 結構速くなった
    - 時間の具体的な見積もり：n = 3000, Python 10^7として　 3000 / 10^7 = 3 * 10**-4

https://github.com/mamo3gr/arai60/blob/105_construct-binary-tree-from-preorder-and-inorder-traversal/105_construct-binary-tree-from-preorder-and-inorder-traversal/step2.py

- 区間を表すclass Spanを作っている
- 無駄がないといういみでは自分の左端とnum_childrenを持つ形でも良さそう
- frontierを使った再帰ループでも書いている

コメント集
https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.1rv0z8fm6lc3

- inorderの順番で構築: https://discord.com/channels/1084280443945353267/1247673286503039020/1300957719074967603
    - C++をPythonに変換した (sol3)
    - inorderで自分より前（自分の左）、preorder自分より後（=自分の子供）のノードをleftでまとめて回収
    - 自分の左は確定しているが、右が確定していないノードをstackに積む。これらはinorderで探索しているので、親が先にstackに入る（後に出る）。よって、これらを右に重ねていけばよい。
    - 自分で書くのは無理

