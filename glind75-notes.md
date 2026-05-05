# [Glind75](https://leetcode.com/problem-list/rab78cw1/)で学んだことのメモ

Arai60と重複しているものは除く

## String

<details>
<summary>0005. Longest Palindromic Substring</summary>

- 部分文字列を全列挙して毎回回文判定すると、候補がO(n^2)、判定がO(n)なので最悪O(n^3)
- 中心から左右に展開すると、奇数長と偶数長の回文をそれぞれ扱えてO(n^2)
- 偶数長回文は`expand(center, center + 1)`で、2文字の間を中心として扱う
- Manacher's algorithmは、
    - 奇数長・偶数長をまとめて扱うために`#a#b#b#a#`のように変換する
    - Manacher's algorithmでは、すでに見つけた右端が最も遠い回文の`center/right`を使い、対称位置の半径から保証できる範囲を再利用する
    - 保証済み半径の外側だけを実際に比較するため、`while`がネストしていても全体ではO(n)
- 関数を切り出すときは、読む人が何に興味があるかを考える

</details>

