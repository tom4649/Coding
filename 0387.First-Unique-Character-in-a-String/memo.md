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

### 解き直し
- 空でもう一度書くとdictを使った解法になった
- sol2のようにOrderedDictも思いつくようにしたい
- queueとdequeの違いについて調べた：
    - `queue.Queue`は複数スレッドから安全に使うためのキューで、内部でlockや条件変数を使う
    - 単一スレッドのアルゴリズム問題では同期処理が不要なので、`queue.Queue`はやや重い
    - `queue.Queue`には先頭を見るための`peek`がなく、`.queue[0]`で内部実装に触るのは避けたい
    - `collections.deque`は両端キューで、`append`, `popleft`, `q[0]`を素直に使える
    - 今回のように先頭を確認しながら古い候補を捨てる用途では`deque`の方が自然