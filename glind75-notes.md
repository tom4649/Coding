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
<summary>0015. 3Sum</summary>

- uniqueな解をどうやって得るか
- whileの重複スキップ: 一致が見つかって `start++` した後に同じ値を飛ばす

</details>


<details>
<summary>0383. Ransom Note</summary>

- hashtableを使う
- 制約をよく見る

</details>


<details>
<summary>0011. Container With Most Water</summary>

- two-pointers の変数のペアリングとしては [start, end) または [first, last] といったものが一般的か。end は含まれず last は含む
- math.infの方がfloat("inf")より自然か
- min-heapをmax-heapとして使う場合、コメントが必要か
- 両端ポインタ, bisect, セグメント木, ヒープと複数の視点からアプローチできる。自分の引き出しの少なさを自覚

</details>


<details>
<summary>0876. Middle of the Linked List</summary>

- slow を1ステップ、fast を2ステップ進めると、fast がリスト末尾に達したとき slow がちょうど中央を指す

</details>


<details>
<summary>0994. Rotting Oranges</summary>

- BFSが定石だと思うがDFSでも解ける
- IntEnumを使うと自然

</details>


<details>
<summary>0017. Letter Combinations of a Phone Number</summary>

- バックトラックを最初の選択肢に
    - 全列挙・組み合わせ系の問題（Subsets, Permutations, Combination Sum, Generate Parentheses）と同じ骨格なので、バックトラック（再帰 + `current` の使い回し）を最初に検討すべきだった
    - イテレーティブ DFS で解いた
- 文字列の構築は `list` + `"".join()` で行う
    - Python の文字列は immutable なので `+=` で連結するたびに新しいオブジェクトを生成し O(n^2) になる
    - `list` に `append` して最後に `"".join()` すれば O(n)

</details>

<details>
<summary>0155. Min Stack</summary>
- Monotonic Stack（単調スタック）
    - スタック内の要素が常に単調増加 or 単調減少になるように維持するデータ構造
    - このMin Stackの `min_data` は単調非増加スタックの一種
    - 典型問題: Next Greater Element・ヒストグラムの最大面積・Trapping Rain Water など
    - O(n^2) の全探索を O(n) に落とせる
</details>


<details>
<summary>0496. Next Greater Element I</summary>

- Monotonic Stack の定石パターン
    - 「右（左）にある最初の大きい/小さい要素」という形の問題に使う
    - 全探索 O(n1 * n2) → Monotonic Stack で O(n1 + n2) に落とせる
- 思考の道筋
    1. 全探索で考える → 同じ要素を何度も走査していると気づく
    2. 視点を逆転：「各要素が答えを探す」→「**各要素が誰かの答えになれるか**」
    3. 未解決の要素を `pending`（スタック）に積んでおき、大きい要素が来たら順次確定させる
    4. スタック内は自然と**単調減少**になる（小さい要素は先に答えが確定してpopされるため）

</details>

<details>
<summary>0981. Time Based Key-Value Store</summary>

- 二分探索によって満たされる条件に注意

</details>


<details>
<summary>0542. 01 Matrix</summary>

- 各マスから最寄りの `0` までの最短距離は **多始点 BFS**（全 `0` をキューに入れて一斉に広げる）で O(mn)。最初に確定する距離が最短になる
- 「各 `1` から BFS」は重複訪問が多く非効率になりやすい。計算量を言語化できると方針を選びやすい
- **2 回走査 DP**: 左上→右下で上・左からの候補、右下→左上で下・右を足す。`1` は未確定を十分大きな `inf` で初期化し、**存在する隣だけ**で `min` する（境界で `inf+1` にしない）
- 多始点 BFS の別形として「`0` に隣接する `1` だけを初期フロンティアにする」もあるが、多くの場合は **全 `0` スタート**の方が実装が素直
- **in-place** に入力行列を書き換える DP もある（省メモリ・入力破壊可のとき）。面接や本番では別配列の方が無難なことが多い
- 「収束するまで全体を緩和し続ける」系は原理の理解用にはなるが、最悪が重く **主戦法には向かない**
- 実装の好み: `visited` 行列と距離行列を分ける／距離を `-1` 未訪問で一本化する、層ごとの BFS とキューに距離を載せる BFS など同値のバリエーションがある

</details>


<details>
<summary>0416. Partition Equal Subset Sum</summary>

- 等和分割は「全体の和が偶数」かつ「部分集合の和が `sum // 2` になるか」の **Subset Sum 判定** に帰着する
- 各要素を使う／使わないの素朴な分岐は $2^n$ で TLE になりやすい
- `(subset_sum, index)` を `functools.cache` などでメモ化すると速くなることもあるが、状態数が膨らみ **MLE** になりうる。目標和は高々約 $10^4$ 程度なので **1 次元 DP** の方が筋がよい
- `reachable[s]`（和 `s` に到達できるか）を更新するとき、同じ `num` を同一段で二度使わないよう **大きい `s` から降順**に回す（0/1 ナップサック）。前段の状態を別配列にコピーしなくてもよい
- DP 配列のコピー忘れ・添字の細かいミスで時間を食いやすい。意味のない `sorted(nums)` は不要（順序は本質ではない）
- 配列は「その和に到達できるか」の真偽なので `reachable` のような名前と、**部分集合和**であることが伝わるコメントにすると読みやすい
- 目標和を `target` として `return reachable[target]` と書くと、`possible_sum[-1]` より意図が明確になりやすい

</details>
