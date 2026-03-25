
# 105. Construct Binary Tree from Preorder and Inorder Traversal

- sol1: 愚直な方針。再帰でpreorderの先頭が根であり、preorderでその位置を特定して再帰。
    - 時間計算量: 根の探索とスライス作成で最悪O(n**2)
    - 空間計算量: スライス作成で最悪O(n**2)
    - 再帰スタック：O(h), 最悪O(n)
- sol2: 再帰は変えずに、inorder の値→index の辞書を作って (O(1)) で位置を引き、再帰は「配列の範囲（左右境界）」で表す（スライスしない）。
    - 時間計算量: 最初の val_to_indexの計算でO(n)
    - 空間計算量: val_to_indexのみなのでO(n)
    - 再帰スタックは上と同じ
    - 結構速くなったので、これが想定解か
- TODO: 他の人の解答をみるなど
