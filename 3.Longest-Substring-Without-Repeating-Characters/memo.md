# 3. Longest Substring Without Repeating Characters

- sol1.py: 自力で解いたが、テストの途中を print するなどデバッグして答えを合わせた

コメント集
- https://github.com/olsen-blue/Arai60/pull/49#discussion_r2005295464
> seen_char_to_index.get(s[right], -1) と使えば、条件分岐を回避できますね。



知らなかった（勉強したことはある気がする）が、初期の実装がこのアルゴリズムになっていた
- 尺取法
    - https://qiita.com/drken/items/ecd1a472d3a0e7db8dce
- sliding window
    - https://qiita.com/rumblekat03/items/4edd9dd4607280c994d1


https://github.com/mamo3gr/arai60/blob/3_longest-substring-without-repeating-characters/3_longest-substring-without-repeating-characters/memo.md

> char_to_index.get(c, -1) として条件分岐をなくす (step2). コードとしてはすっきりするけど、読み手からしたらシミュレートの手間が増えそう。

という考えもあるのか。

sol2.py: 他の人のコードとコメントを参考にもう一度書き直す
