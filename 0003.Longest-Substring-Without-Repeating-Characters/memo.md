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

## 尺取法と sliding window

### sliding window

配列・文字列のような線形なシーケンスに対して、**「窓 (window) = 連続した区間 `[left, right]`」を左から右へ滑らせながら答えを更新する**設計パターンの総称。

- **固定長 sliding window**: 窓のサイズが定数 `k` で固定
    - 例: 「長さ `k` の連続部分配列の和の最大」
    - 1 ステップごとに `right` を 1 進め、`left` も 1 進めて長さを保つ
- **可変長 sliding window**: 窓のサイズが「条件を満たす最大／最小」で決まる
    - 例: この問題（重複なしの最長部分文字列）、「和が `K` 以下となる最長区間」など
    - `right` を伸ばすと条件が厳しくなり、`left` を進めると条件が緩くなる、という単調性のある問題に適用できる

尺取法 (caterpillar method, two pointers)：可変長 sliding window の日本語名

ポイントは:

1. **両ポインタは単調に増加する方向にしか動かさない（戻さない）**
2. 各ポインタの 1 ステップは O(1) ないし amortized O(1)
3. → ループは見た目二重でも、各ポインタが最大 n 回しか進まないので **合計 O(n)**（償却計算量）
