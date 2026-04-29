# Coding

<details>
<summary>0141.Linked List Cycle</summary>

- `set`を使った解法
- `set`と`dict`がどちらもhashtableで値を格納している
- そのためdictのkeyはhashableである必要がある
- `__eq__` が `True` なら、`__hash__` も等しくなければならない

</details>
<details>
<summary>0142.Linked List Cycle II</summary>

- Floydの循環検出法（有名だが常識ではない）
- `is`と`==`の違い: オブジェクトの同一性を比較する。同じインスタンスかどうか
    - `is`: オブジェクトの同一性を比較する。同じインスタンスかどうかを`id()`で判定（CPythonではメモリアドレスとして実装されている）。
    - `==`: `__eq__`でオブジェクトの等価性を比較する。

</details>
<summary>83.Remove Duplicates from Sorted List</summary>

- Linked Listの操作
- 変数名には組み込み名と衝突する名前を使わない

</details>

<summary>82.Remove Duplicates from Sorted List II</summary>

- 変数名の意味を考える
- currentの名前は情報量がない
- dummyを番兵として用いる方法は自然に解釈できる

</details>
