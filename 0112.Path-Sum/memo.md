# 112. Path Sum
[リンク](https://leetcode.com/problems/path-sum/description/)

- sol1.py: 再帰で書いたが少し遅い

- https://github.com/SuperHotDogCat/coding-interview/pull/37#discussion_r1665891252
> これ、引き算先にしちゃって、
- これはできた

- https://github.com/naoto-iwase/leetcode/pull/29/changes#r2455081026
    - パスを保存する状況を聞かれる可能性
    - 解答が良さそう
> そうですね、通ったノードのその時点の和を記録するsetまたは辞書を持つようにし、ゴールの葉からスタートに向かって再びBFS/DFSするのが（空間）計算量が節約できて良さそうですね。

> さらに、そのようなpathの総数/pathを全部知りたい場合は、1回目の前向きの探索をearly returnなしで完遂し、和の記録も通った回数を辞書で記録しておくのが良さそうに思います。


- sol2.py: スタックを使った実装も一応書いておく
