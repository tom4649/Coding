# 387. First Unique Character in a String

- 愚直な実装（sol1.py）は2回文字を見る
- https://discord.com/channels/1084280443945353267/1233603535862628432/1238208008182562927
    - 文字が一回しか流れてこない場合を考えたい(sol2.py)
    - Ordered dictを使うと書ける
    - 速くなった

- Queueも使う実装もある
    - https://github.com/colorbox/leetcode/pull/29/changes/BASE..48f2749be9c4ec78c6f24c887880e34c7206f678#r1861430039
    - sol3.py
    - queue.Queueにはpeek（先頭の覗き見）がない
    - queueメソッドを使ったが推奨されないと思う
    - dequeを使うのが良い気がする
- OrderedDictの実装はdoubly-linked list
    - 実装した (sol4.py)
    - 参考：https://gist.github.com/joequery/12332f410a05e6c7c949
    - "Doubly"によって前の参照ができることにより、削除をO(1)で実行可能
    - 「これ、OrderedDict の中身は Doubly-Linked List なので、まあ、練習としては、Doubly-Linked List 自体を書いて欲しいところではありますね。」
