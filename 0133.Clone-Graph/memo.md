# 133. Clone Graph

hashmap + DFSを使った解法: sol1.py
珍しくミスなく一発で通った

`dict.get(key, default)` はデフォルト値を**常に評価**するため、`Node(...)` のような生成コストがある場合は `if key not in dict` で分岐するほうがよい

改善: sol1_revised.py


### 他の人のコード
https://github.com/huyfififi/coding-challenges/pull/32

C++に関する記述は読んでいない。
C++の練習も始めるのはありかもしれない。

再帰でも書く: sol2_recursive.py
スタックに入れるノードの数を一つにする

deepcopyでも解けることに気が付く: sol4.py

内部で同様のメモ化付き再帰トラバーサルを行っており、汎用性のための型チェック・pickle プロトコルのオーバーヘッドがある

https://github.com/python/cpython/blob/main/Lib/copy.py#L110

deepcopyの実装
atomicの場合にはそのまま返すこと、memoが使われていることを確認した

