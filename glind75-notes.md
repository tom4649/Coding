# [Glind75](https://leetcode.com/problem-list/rab78cw1/)で学んだことのメモ

Arai60と重複しているものは除く


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


<details>
<summary>0133. Clone Graph</summary>

- グラフのクローンは hashmap（`original → copy`）+ グラフ探索（DFS/BFS）で解く
- hashmap がサイクル検出と cloneノードの参照の両方を兼ねる
- ノードを hashmap に登録するタイミングは、neighbors を処理する**前**（後にすると再帰・ループで同じノードを二重処理してしまう）
- `dict.get(key, default)` はデフォルト値を**常に評価**するため、`Node(...)` のような生成コストがある場合は `if key not in dict` で分岐するほうがよい
- `copy.deepcopy` でも解けるが、内部で同様のメモ化付き再帰トラバーサルを行っており、汎用性のための型チェック・pickle プロトコルのオーバーヘッドがある
- 真偽値を返す関数で、条件分岐で返り値が変わる場合、条件それ自体を返り値とする
</details>


<details>
<summary>0383. Ransom Note</summary>

- hashtableを使う
- 制約をよく見る

</details>
