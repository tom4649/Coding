# 133. Clone Graph

hashmap + DFSを使った解法: sol1.py
珍しくミスなく一発で通った

`dict.get(key, default)` はデフォルト値を**常に評価**するため、`Node(...)` のような生成コストがある場合は `if key not in dict` で分岐するほうがよい

改善: sol1_revised.py


### 他の人のコード
https://github.com/huyfififi/coding-challenges/pull/32


再帰でも書く: sol2_recursive.py
スタックに入れるノードの数を一つにする: sol3.py

deepcopyでも解けることに気が付く: sol4.py

内部で同様のメモ化付き再帰トラバーサルを行っており、汎用性のための型チェック・pickle プロトコルのオーバーヘッドがある

https://github.com/python/cpython/blob/main/Lib/copy.py#L110

deepcopyの実装
atomicの場合にはそのまま返すこと、memoが使われていることを確認した

### 解き直し

つまるところはなかった。

ユーザー定義のクラスインスタンスのハッシュが id に基づいて決まることを確認した。つまり、この問題では同じval, neighborsのインスタンスでもハッシュは異なる。

https://docs.python.org/ja/dev/glossary.html#term-hashable

> ユーザー定義のクラスのインスタンスであるようなオブジェクトはデフォルトでハッシュ可能です。 それらは全て (自身を除いて) 比較結果は非等価であり、ハッシュ値は id() より得られます。

