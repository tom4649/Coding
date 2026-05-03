# 695. Max Area of Island
- 前の問題をdfsで解いたのでbfsで解いた(sol1.py)
    - `for delta in [1, -1]:`で書くより、diretionsを4つ書き出した方が可読性は高いのかもしれない
    - そこだけ書き直した(sol2.py)
- UnionFind
    - https://github.com/mamo3gr/arai60/blob/main/695_max-area-of-island/step2.py
    - 小さい集合を大きい集合に付け加える
    - この場合、adjacentは片側だけで良い
    - かなり時間がかかったので、後で解き直したい
- いずれにしても計算量 O(mn) は避けられない

