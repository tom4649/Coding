# Coding

<details>
<summary>78. Subsets</summary>

- バックトラック再帰
- Iterative doubling
    - 観察: `subsets({a, b, c}) = subsets({a, b}) ∪ {S ∪ {c} | S ∈ subsets({a, b})}`
    - 実装は驚くほど短い

- **lazy iterator 版**
    - **`itertools.tee(it, n)`**: 1 つのイテレータを `n` 個の独立したイテレータに分割。一方が先に進むと内部バッファに保持されるので、消費が大きくずれるとメモリも食う
    - **デフォルト引数で値をキャプチャするイディオム**

```python
results = itertools.chain(a, map(lambda s, v=value: s + [v], b))
```
        - Python の `lambda s: s + [value]` だと、ループ内のすべての lambda が**同じ `value` 変数**を参照してしまう（**遅延評価 / late binding**）
        - `v=value` のように **デフォルト引数**にすると、関数定義時に `value` の現在値が評価され、各 lambda に「束縛された値」として保持される
        - 公式ドキュメントより:
          > デフォルト引数値は関数定義が実行されるときに左から右へ評価されます
          - <https://docs.python.org/ja/3/reference/compound_stmts.html#function-definitions>
- Python の引数渡しの呼び方
    - Python は **call-by-object (参照の値渡し)**: 「オブジェクトへの参照を値としてコピーして渡す」
    - **call by value**: 実引数を 1 度評価して、値（のコピー）を仮引数に束縛
    - **call by name**: 実引数は呼び出し時には評価せず、関数本体で名前が使われるたびに元の式を再評価
    - デフォルト引数の話は「評価戦略」というより、「**デフォルト引数式がいつ評価されるか**」の話

</details>
