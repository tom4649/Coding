# 776. Split BST

再帰で書いた: sol1.py
特に詰まるところはなかった
計算量: 時間 O(n) 空間 O(n)だが平衡ならばO(logn) (木の高さ)
破壊的で書いたが非破壊的にするためにはdeepcopyをすればよい

### コメント集
https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.3czeid3ovy2a

https://discord.com/channels/1084280443945353267/1237649827240742942/1327643938567360555

> 再帰とループの中間を念頭において、対応関係から相互に変換できるようにしておくといいでしょう。一例として、中間に来るものは、このような感じです。

sol2.pyを書いたがわかりづらいかもしれない
外から変更できるようにListを用いた
30分ぐらいかかった...

### 他の方のコード

https://github.com/naoto-iwase/leetcode/pull/48/changes/BASE..ce3bd07a6b3bc839e7e3e486932ec858884f8a73#diff-bf4c07f093e9b7197d01187d81e45a9d076a1028227be3ed6ba9df6745f3950b

このstep3とほぼ同じ回答。

https://github.com/mamo3gr/arai60/blob/776_split-bst/776_split-bst/memo.md

ループで書いている
考え方はsol2.pyに近い
