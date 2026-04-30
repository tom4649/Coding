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

<details>
<summary>83.Remove Duplicates from Sorted List</summary>

- Linked Listの操作
- 変数名には組み込み名と衝突する名前を使わない

</details>

<details>
<summary>82.Remove Duplicates from Sorted List II</summary>

- 変数名の意味を考える
- currentの名前は情報量がない
- dummyを番兵として用いる方法は自然に解釈できる

</details>


<details>
<summary>0002.Add Two Numbers</summary>

- 多倍長整数の加算

</details>

<details>
<summary>20. Valid Parentheses</summary>

- PEP-8 と Google Style Guide では strings, lists, tuples は implicit で真偽判定
- 副作用のある式を条件のところに書かない方が良いかもしれない。読む側が頭の中で実行順序を追う必要が出るため。e.g. `stack.pop()`

</details>

<details>
<summary>206. Reverse Linked List</summary>

- 一度の走査で行うポインタの付け替え

</details>
<details>
<summary>703. Kth Largest Element in a Stream</summary>

- heapqライブラリの使い方
- マージソート、クイックソート、クイックセレクトの確認
- ヒープの構築がO(n)であることが抜けていた

</details>
<details>
<summary>347. Top K Frequent Elements</summary>

- ヒープの構築はO(n) (再)
- クイックソートの実装
- 一行で行う操作を増やしすぎない

</details>


