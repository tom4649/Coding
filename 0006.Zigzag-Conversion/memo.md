# 6. Zigzag Conversion


上の行からどの位置に対応するかを考えて順に詰めていく: sol1.py

ロジックを変えずにリファクタリング: sol2.py
変数名にも気をつかったつもりではいる

### コメント集
https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0

https://github.com/Mike0121/LeetCode/blob/main/Arai60-ReviewEdition/6.%20Zigzag%20Conversion.md

素直にzigzagに文字列を並び替えるのをシミュレートしている

> Generator を使ってインデックスの生成を分けるアイディア

https://github.com/saagchicken/coding_practice/pull/22#discussion_r2009413184

> （標準ライブラリを）1ヶ月に1回でも見ている人と、見る癖がない人、話してみれば区別がつくと思いませんか。

標準ライブラリを見る癖をつけたい

> Generator expression で、さらに二重にもできます。

`"".join(["".join(line) for line in display_board])`から`"".join(c for line in display_board for c in line)`に変換している

> この問題、出題意図は、お手玉できるか、な気もします。
> Generator は内部的には、ある種のコンテキストを持っていて、計算の続きに戻れるようにしています。だから、それなりに重いです。
> そういうわけで、手続き型の手法で構造を組み合わせられるかが想定だろうなと思います。
> 「手作業で簡単にできることを、基本的な文法を使って、自分の言葉でコードにすることができますか」

素直な手続きで書くべきだったのかもしれない。自分のsol1.py, sol2.pyはパズルを解いたような解法なので読み手が理解しにくい

> Java や Python など文字列が immutable な言語では重要な話ですが、C++ では、mutable で後ろに文字をつける分には大きな問題になりません。

> 前後に付けたり分割したりなどする必要があるならば、Rope というデータ構造などを使えばいいですが、そこまでする必要があることは少ないです。

Rope: https://blog1.mammb.com/entry/2025/11/22/000000

文字列をチャンクに分割し、チャンク毎の長さをテキスト先頭からの位置を表す二分木

> itertools.batched とか

https://github.com/olsen-blue/Arai60/pull/61/changes/BASE..f093181010b887d9cafa28a885ca63fc2b699566#diff-ccfa5b3e70552f7a1aea1f6a719cd00d74a1035c89cfab6426fddc4696ed3e21

https://docs.python.org/ja/3/library/itertools.html#itertools.batched

3.12からの新機能らしい

Generator を用いて書く: sol3.py
