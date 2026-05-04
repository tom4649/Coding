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

<details>
<summary>98. Validate Binary Search Tree</summary>

- 木の探索順（preorder, inorder, postorder）
- 再帰とループの変換
- ロジックの流暢さ

</details>
<details>
<summary>373.Find K Pairs with Smallest Sums</summary>

- 全組み合わせを作らず、次に小さくなりうる候補だけをヒープで管理する
- 分からない場合には手作業で考える

</details>

<details>
<summary>1. Two Sum</summary>

- Hashmapを使うと、必要な相手の値を平均O(1)で確認できるため、全探索のO(n^2)をO(n)に改善できる
- Type HintsはPython3から導入され、Docstringの型指定が使われなくなった
- 実装から時間計算量を見積もる時の目安
    - C++： 約 1～10 億 (10^8~10^9) ステップ/秒、Python： 約 100 万～1000 万 (10^6~10^7) ステップ/秒

</details>

<details>
<summary>49. Group Anagrams</summary>

- 理論上は文字頻度を使う方が速いが、Pythonの組み込みsortはC実装で高速なので、入力サイズによってはsortedを使う方が実測で速いことがある
- listはmutableでhashableではないため、dictのkeyにするにはtupleへ変換する必要がある

</details>

<details>
<summary>349. Intersection of Two Arrays</summary>

- setはhash tableで実装されており、構築は平均O(n)、membership checkは平均O(1)
- 短い方をsetにすると、空間計算量をO(min(l1, l2))に抑えられる
- 入力がソート済み、片方だけ巨大、メモリ制約が厳しいなど、追加条件によって適した解法は変わる
- ソート済み配列同士なら、マージソートのmergeに近いtwo pointersでO(l1 + l2)
- マージソート
    - pros: 最悪計算量もO(n log n)で安定、stable sort、外部ソートに向く
    - cons: 配列では追加メモリO(n)、コピーの定数倍が重い、実測ではquick sortより遅いことが多い


</details>


<details>
<summary>929. Unique Email Addresses</summary>

- `str.partition`: 区切り文字で「左、
区切り文字、右」の3要素に分けるため、最初の1回だけ分割したい意図を表しやすい
- 正規表現、有限ステートマシン、文字列操作の複数方針
- Pythonの文字列はimmutableなので、ループ内での文字列連結は避け、必要ならlistにappendして最後に`"".join()`する

</details>

<details>
<summary>387. First Unique Character in a String</summary>

- 頻度を先に数えてから再走査する解法はシンプルで堅いが、文字列を2回見る
- 文字が1回しか流れてこない設定では、現在ユニークな文字だけを順序付きで管理する発想が使える
- `OrderedDict`は挿入順を保てるため、重複した文字を削除していけば先頭が最初のユニーク文字になる
- `queue.Queue`はスレッド同期用の機能を持つため、単一スレッドのアルゴリズム用途では`collections.deque`の方が自然
- `queue.Queue`には`peek`がないので、先頭を見ながら取り除く用途では`deque`の`q[0]`と`popleft()`が使いやすい
- `OrderedDict`の順序管理は、dictに加えてdoubly-linked listを持つことで実現できる
- doubly-linked listでは前後の参照を更新することで、ノード削除をO(1)で行える

</details>

<details>
<summary>560. Subarray Sum Equals K</summary>

- prefix sumの出現回数をhashmapで管理すると、全区間を列挙するO(n^2)ではなくO(n)で数えられる
- 累積和配列を作って後から処理するより、走査しながら過去のprefix sumを数える方がシンプルに書ける
- 和がKになる区間を列挙する問題に変えると、prefix sum同士の対応関係を理解しやすい
- `defaultdict(int)`を使うと、存在しないprefix sumの出現回数を0として扱えて実装が素直になる
- パフォーマンス不足はデータ量が増えたときに実行時間やメモリ使用量として現れるため、O(n^2)からO(n)への改善は実務でも効く

</details>
<details>
<summary>200. Number of Islands</summary>

- DFSでは再帰でも書けるが、探索が深い場合はコールスタックの上限に注意が必要
- 明示的なstackを使うと再帰を避けられ、深い探索でも扱いやすい
- 訪問済みの印は、gridを書き換える方法と`seen`集合で管理する方法がある
- gridを書き換える場合は、帰りがけではなく行きがけで印をつけると無限ループを防ぎやすい
- gridを書き換えると破壊的になってしまう
- 境界判定や隣接マスの列挙は関数に分けると、グリッド探索の本体が読みやすくなる
- 添字の変数名は`i`, `j`よりも`row`, `col`にすると、行と列の意味が明確になる
- BFSは最短経路、DFSは連結成分・トポロジカルソート・サイクル検出などに応用しやすい
- UnionFindでも解けるが、問題側の操作に合った抽象を用意しないと使う側の負担が大きくなる
    - 汎用的なUnionFindは自然数の添字同士をつなぐだけなので、呼び出し側が`row * num_cols + col`への変換や陸地判定を担当することになる
    - 問題寄りのAPIを用意すると、呼び出し側が楽に書ける
- メソッドは呼び出し側に強い前提を押しつけず、多少雑に呼ばれても扱える設計が望ましい

</details>

<details>
<summary>695. Max Area of Island</summary>

- 島の最大面積も、グリッド上の連結成分をDFS/BFSで探索して各成分のサイズを数えればよい
- stackやqueueに同じマスを重複して積みたくない場合、`seen`は「処理済み」ではなく「発見済み」として、stack/queueに入れるタイミングで更新する
- `seen`をpop後に更新する書き方もできるが、その場合はpop直後に処理済みならskipしないと面積を二重に数えてしまう
- UnionFindでも解けるが、各マスは上下左右すべてではなく右と下だけを見れば隣接関係を重複なく結合できる
- どの解法でも全マスを確認する必要があるため、時間計算量はO(mn)

</details>

<details>
<summary>127. Word Ladder</summary>

- 単語をノード、1文字だけ違う関係を辺と見ればグラフの最短経路問題として扱える
- 全単語ペアを比較して隣接リストを作ると、前処理がO(N^2 L)になって遅い
- `subword`を使って`h*t`のような形から隣接候補を引くと、全ペア比較を避けられる
- 各位置を`a-z`に置き換えて候補を作り、`set`で存在確認する方法もある
- `set`は未訪問の有効単語集合としても使えるため、見つけた単語を削除すれば`seen`を別に持たずに済む
- `discard`は存在しない値を削除しようとしても何もしないが、`remove`は`KeyError`になる
- 双方向BFSでは常に小さいfrontierから広げることで探索量を減らせる

</details>

<details>
<summary>104. Maximum Depth of Binary Tree</summary>

- 二分木の最大深さは、左右の部分木の最大深さを求めて大きい方に1を足すボトムアップ再帰で自然に書ける
- トップダウン再帰では、現在の深さを引数で渡しながら全ノードをたどり、外側の`max_depth`を更新する
- 内側関数から外側の変数に再代入する場合は`nonlocal`が必要になる
    - 外側の変数を参照するだけなら`nonlocal`は不要
    ```python
    def outer():
        x = 1

        def inner():
            return x

        return inner()
    ```
    - しかし、同じ内側関数内で代入すると、Pythonはその名前を内側関数のローカル変数とみなす
    ```python
    def outer():
        x = 1

        def inner():
            x = x + 1  # UnboundLocalError
            return x

        return inner()
    ```
    - 外側の変数を更新したい場合は`nonlocal`で明示する
    ```python
    def outer():
        x = 1

        def inner():
            nonlocal x
            x = x + 1
            return x

        return inner()
    ```
    - `max_depth = max(max_depth, depth)`も同じで、`nonlocal`なしだと右辺の`max_depth`まで内側関数のローカル変数扱いになり、代入前参照で`UnboundLocalError`になる
- LeetCodeの指定シグネチャにある引数名は、Pythonではkeyword呼び出しのAPIにもなり得るため、安易に変えない方がよい

</details>

<details>
<summary>111. Minimum Depth of Binary Tree</summary>

- 最小深さは根から浅い順に見るBFSと相性がよく、最初に見つけた葉の深さをそのまま返せる
- DFSで解く場合は、全探索しながら最小値を更新するトップダウン再帰か、左右の部分木の答えを集約するボトムアップ再帰で考えられる
    - トップダウンは、現在の深さや根からの累積情報を引数で子へ配る
    - ボトムアップは、書きやすい
- 再帰DFSは木が深いとコールスタック上限に当たる可能性があるため、深い入力があり得るならBFSや明示的なstackも検討する
- `None`だけを判定したい場合は、PEP 8やGoogle Python Style Guideの考え方に沿って`if node.left is None:`のように書く

</details>

<details>
<summary>617. Merge Two Binary Trees</summary>

- `copy.copy`は浅いコピーなので、親ノードだけが新しくなり、`left`や`right`の子孫ノードは元の木と共有される
- `copy.deepcopy`は深いコピーなので、`left`や`right`からたどれる子孫ノードも再帰的に複製される
- immutableなオブジェクトでは浅いコピーと深いコピーの差はほぼ問題にならないが、listやTreeNodeのように内部に別オブジェクトへの参照を持つ複合オブジェクトでは差が出る

</details>

<details>
<summary>112. Path Sum</summary>

- 問題自体は再帰で素直に解ける
- パスを返す/数える発展
    - 経路自体を返したい場合は、各ノードで「親ノード」または「そこまでの累積和」を辞書/setに記録しておけば、目的の葉から遡って経路を再構成できる
    - 経路の総数や全列挙が必要なら、early returnせずに最後まで探索し、累積和の出現回数を`defaultdict(int)`で集計するのが良い

</details>

<summary>108. Convert Sorted Array to Binary Search Tree</summary>

- ソート済み配列の中央を根にして、左右の半分から部分木を再帰的に作るのが一番素直
- スライス `nums[:idx]`, `nums[idx+1:]` で書くとシンプルだが、コピーが発生するため空間計算量がO(n log n)になる

</details>

<details>
<summary>102. Binary Tree Level Order Traversal</summary>

複数の解法が考えられる。

- 帰りがけDFS再帰（部分木の結果をmergeする）
    - 左右の部分木のlevel orderを再帰で求めてから、`itertools.zip_longest`で同レベル同士を連結する
    - 時間計算量: 偏った木でO(n^2)（各レベルで`left + right`のリスト連結がかさむ）
    - 空間計算量: 結果のO(n) + 再帰スタックのO(h)
    - 計算量も悪化するので、積極的に選ぶ理由は薄い

- 行きがけDFS再帰（レベルを引数で配る）
    - `level`を引数で渡し、`level_order[level]`に値を直接appendする
    - 時間計算量: O(n)
    - 空間計算量: 結果のO(n) + 再帰スタックのO(h)
    - 短く書けるが、深い木ではPythonの`sys.setrecursionlimit`に当たる/Cスタックを破壊するリスクがある

- 行きがけDFS反復（明示stack）
    - 上を明示スタックに書き直したもの。`deque.pop()`でDFS
    - 左から処理したい場合、子は`(node.right, node.left)`の順で積む（後入れ先出しのため）
    - 時間計算量: O(n)
    - 空間計算量: 結果のO(n) + スタックのO(h)
    - 再帰深さの上限を気にせず使え、ログも取りやすい

- BFS（queue + level_size）
    - 各反復で`len(queue)`を先に保存し、その回数だけ`popleft`して現レベルを取り出す
    - 時間計算量: O(n)
    - 空間計算量: 結果のO(n) + キューの最大幅（最悪O(n)）
    - 「レベルごとの処理」が問題の構造そのものと一致するため最も読みやすい
    - 最短深さや「最初に条件を満たす階層」を返したい派生問題にも素直に拡張できる

- 例外処理は「if-elseで両方の場合を書く」より「ifで例外だけ早期returnし、本流のロジックを後ろにフラットに書く」のが読みやすいことがある
- 再帰の上限はPythonでは`sys.setrecursionlimit`が言語処理系側でガードする。Javaのスタックは~1MB、Cは~10MBが目安
- 再帰は「ある条件のときだけログを出して呼び出し元を追う」のが難しい。ループに直すとデバッグしやすい
- クイックソートで小さい方を再帰、大きい方を末尾再帰で処理するのも、スタック深さ抑制のため
<summary>108. Convert Sorted Array to Binary Search Tree</summary>

- ソート済み配列の中央を根にして、左右の半分から部分木を再帰的に作るのが一番素直
- スライス `nums[:idx]`, `nums[idx+1:]` で書くとシンプルだが、コピーが発生するため空間計算量がO(n log n)になる


<details>
<summary>103. Binary Tree Zigzag Level Order Traversal</summary>

- 102（level order）に「奇数段だけ向きを反転」を足した派生問題と捉えると、102のBFS解にreverseを1行足すだけで済む
- リストを「逆順」に扱う方法は用途で選ぶ
    - `xs.reverse()`：破壊的（in-place）。リスト自体を反転して構わない場面で最有力
    - `reversed(xs)`：非破壊の逆順イテレータ。`for`で回すだけならコピー不要で軽い（返り値はイテレータ）
    - `list(reversed(xs))` / `xs[::-1]`：非破壊で「反転した新しいリスト」が欲しいとき（どちらも O(n) コピー）
    - 手動の`for i in range(len(xs)-1, -1, -1)`：特殊な制御が要るときだけ。可読性は落ちがち

</details>

<details>
<summary>300. Longest Increasing Subsequence</summary>

- 愚直DPだと計算量 O(n^2)
- 二分探索でも解ける O(n log n)
- セグメント木: 元の DP 漸化式 の `max` を区間 max クエリで O(log n) に高速化。全体 O(n log n)
    - 「値の小ささ」は座標圧縮した index の範囲で、「並び順の前後」は `nums` を順に for で回すことで、別々に分担させる
    - 1-indexed のセグメント木では「奇数 = 右の子、偶数 = 左の子」となり、区間 max のループ条件が綺麗に書ける
- Binary Indexed Tree (Fenwick Tree): セグメント木の特殊版で、「常に左端からの累積（prefix）」だけを扱うと決めれば配列サイズを半分（n+1）にできる
    - `index & -index` で親/子に O(1) で移れる（lowbit）。実装は短いが、prefix 系の操作しかできないのが制約
- bisect の挙動
    - `bisect_left(a, x)`: `a[:i]` がすべて `< x` となる最小の `i`（既存の `x` の左）
    - `bisect_right(a, x)`: `a[:i]` がすべて `<= x` となる最小の `i`（既存の `x` の右）
    - `a` に `x` がなければ両者は一致

</details>

<details>
<summary>53. Maximum Subarray</summary>

- 「ある位置 `i` を末尾とする部分配列の最大和」を順に求めれば、その全体の最大が答えになる、という発想で O(n) になる
- 同じことを2通りの式で書ける（どちらも O(n)、空間 O(1)）
    - prefix sum
        - `min_cumulative_sum` の初期値を 0 にすることで、「途中から始める」と「先頭から始める」を統一して扱える
    - Kadane版のアルゴリズム
        - 直感的には「過去の合計がマイナスなら相続をやめる」

</details>

<details>
<summary>62. Unique Paths</summary>

- メモ化再帰で`functools.cache` を使うと再帰関数のメモ化を1行で書ける
- Python のリスト掛け算
  - `[1] * 10` のように immutable な要素を掛け算で並べるのは安全
  - `[[1]] * 10` のように mutable オブジェクトを掛け算で並べると、全要素が同じオブジェクトを指すため一箇所の変更が全体に波及する
  - 2次元配列を作るときは `[[1] for _ in range(n)]` のように内包表記で個別生成するのが安全
  - リストはオブジェクトへのポインタを持っており、immutable は再代入で別オブジェクトに差し替わるが mutable はその場で書き換わる、という違いが原因

</details>


<details>
<summary>63. Unique Paths II</summary>

- 配る DPと もらう DP
  - もらう DP: `dp[r][c]` を「自分が上 / 左から受け取る値」で計算する（一般的）
  - 配る DP: `dp[r][c]` の値を「右と下のマスへ加算する」形で書く
- コンパイラ言語とインタプリタ言語での `if` 分岐コストの違い
  - C / Rust などのコンパイラ言語では、分岐予測失敗で命令パイプラインのやり直しが発生するため、`for` の中の `if` はなるべく減らす方が速い
  - 「0 行目／0 列目だけの特殊処理」など事前に決まっている分岐は、ループの外に出して別ループで処理した方が、可読性も速度も向上する
  - Python はインタプリタ実行で元から大量の分岐命令を踏むので、ここを気にしても差は出にくい（可読性の観点では分けてもよい）
<summary>105. Construct Binary Tree from Preorder and Inorder Traversal</summary>

- preorderの先頭が根、inorderで根の位置がわかれば左右の部分木のサイズが決まる、という性質をそのまま再帰に落とせる
- 改善: inorderの「値 → index」辞書を前計算してO(1)で根の位置を引き、再帰には「配列の範囲（左端 + 子の数、もしくは左端・右端）」を渡してスライスを避けると、時間O(n)・追加空間O(n)になる
- 別解として、inorderの順番でノードを生成し、stackに「.rightが未確定のノード」を積んでいく構築法もある
    - inorderで自分より前にあり、preorderで自分より後にあるノードを.leftにまとめて回収する
    - 親が先にstackに入る性質を使い、自分よりpreorder順で前のノードまでpopして.leftに連結する
    - 思いつくのは難しい

</details>

<details>
<summary>198. House Robber</summary>

- DP配列のメモリは O(n) → O(1) に落とせる
- 変数の意味はコメントで明示すると読みやすい
- メモ化再帰は `@functools.cache` を使うと1行で書ける
- `functools.lru_cache` / `functools.cache` のキャッシュはスレッドセーフ
    - 内部でロックを取っているので、複数スレッドから同じ関数を実行してもキャッシュ自体の状態は壊れない
</details>

<details>
<summary>213. House Robber II</summary>

- 円環の制約は「場合分けで消す」ことで直線版に帰着できる
    - 思考の型: 「未知のものは何か」「与えられているものは何か」「条件は何か」を整理し、厄介な条件を場合分けで消せないか考える
- DP の用語の整理
    - DP は「部分構造最適性」と「部分問題の重複」を持つ問題に対し、「一度計算した部分問題は保存して使い回す」設計指針の総称
    - 実現方法は2つ
        - **Tabulation (タビュレーション)**: ボトムアップ・反復型。DP 配列を小さい方から埋めていく
        - **Memoization (メモ化再帰)**: トップダウン・再帰型。必要になった部分問題を再帰で計算しキャッシュする
- スワップを多重代入で書く（再掲）
    - `a, b = new_a, new_b` の形にすれば、入れ替え用の一時変数を持たずに同時更新できる
- `functools.reduce` で副作用のない関数型スタイルに置き換えられる
    - `reduce(func, iterable, initial)` は他言語でいう `fold_left` と同じで、状態を引数として持ち回り再代入を消せる
    - 可読性は落ちる代わり、ループ内の代入による副作用が無くなり、状態遷移を関数として切り出せる
- `itertools.islice` でスライスのコピーを避ける（`sol2.py`）
    - 新しいリストを作る場合 O(k) のコピーが発生する
    - `itertools.islice(nums, 1, len(nums))` は元のリストをコピーせず遅延評価のイテレータを返すので、メモリも時間も節約できる
    - 引数として一度走査するだけで済むようなケースでは、スライスより `islice` が向いている
- list slice の計算量
    - `nums[a:b]` は要素 `b - a` 個ぶんの新しいリストを作るため O(b - a) の時間と空間がかかる
    - <https://wiki.python.org/moin/TimeComplexity> に基本演算の計算量がまとまっている
</details>

<details>
<summary>121. Best Time to Buy and Sell Stock</summary>

- `itertools.accumulate(prices, min)` で「その日までの最小値」を遅延列として作れる（`sol3.py`）
    - Haskell の `scanl1 min` 相当。関数型風に「最小列 → 利益列 → max」と書ける
    - <https://docs.python.org/ja/3/library/itertools.html#itertools.accumulate>
    - 同じ問題を「scanl で累積最小、zipWith (-) で利益、max で集約」と分解できる
- import スタイル（Google Python Style Guide）
    - `from itertools import islice` のように個別の関数を import するのではなく、`import itertools` してから `itertools.islice(...)` と書く方が好まれる
    - > Use import statements for packages and modules only, not for individual types, classes, or functions.
- 型ヒント
    - Python 3.9+ では `typing.List[int]` より組み込みの `list[int]` が推奨
    - 引数はより抽象的な型（`Sequence`, `Iterable`）、返り値はより具体的な型（`list[int]`）にすると、呼び出し側の自由度を上げつつ、利用側に確かな情報を返せる
</details>

<details>
<summary>122. Best Time to Buy and Sell Stock II</summary>
- 答えは \( \sum_{k=1}^{n-1}\max(0, p_k - p_{k-1}) \) と書ける
</details>

<details>
<summary>139. Word Break</summary>

- `s[start:].startswith(word)` のようなスライスは、毎回新しい文字列オブジェクトを生成する O(n−start) のコピー が発生する。代わりに `s.startswith(word, start)` を使えば追加メモリなしで比較できる。同様に `s[start:end] == word` よりも `s.startswith(word, start)` の方が速い。
- `str.startswith` は tuple を受け取れる

```python
s.startswith(("apple", "pen"))  # どれかで始まれば True
```

-  正規表現的な見方
    - `((apple)|(pen))*` のように正規表現で書ける問題は、`wordDict` を定数とみなせば NFA/DFA 的に O(n) で解ける
- `dataclasses.field(default_factory=...)`
    - `list` / `dict` / `set` のような mutable をフィールドのデフォルト値に直接書くと、`@dataclass` は `TypeError` を出す。インスタンスごとに独立した mutable を持たせたい場合は `default_factory` を使う

</details>

<details>
<summary>322. Coin Change</summary>

- `math.isinf`を用いた判定
- `min` を取るときの工夫
    - 子の結果を generator で流し、`min(gen, default=-1)` で集約すると、無効値を一切流さずに書ける
    - `min` / `max` は `default` 引数で「空イテラブルのときの値」を指定できる

</details>

<details>
<summary>35. Search Insert Position</summary>

- 標準ライブラリで一発: `bisect.bisect_left(nums, target)` と等価な問題
- 区間の取り方を最初に決める
    - 半開区間 `[left, right)` がおすすめ
        - 初期値: `left = 0`, `right = len(nums)`（`right` は配列外を含めて良い）
        - ループ条件: `left < right`
        - ループ不変条件: `i < left ⇒ nums[i] < target` かつ `j >= right ⇒ nums[j] >= target`
        - 終了時 `left == right` で、これが「最初に `True` の位置」 = 答え
    - 閉区間 `[left, right]`（`sol2.py`）は `right = len(nums) - 1` から始まり、`right - left > 1` で抜けて末尾を別途見るなど、境界処理が増える
- `+1` がどこに入るか（半開区間 `[left, right)` の場合）
    - **`nums[mid] < target` のとき**（右に狭める）
        - `mid` は確定で `False` 側 → 次の区間に**含めたくない**
        - 左端は閉区間なので「`mid` を含めない」には `left = mid + 1`（**+1 が要る**）
    - **`nums[mid] >= target` のとき**（左に狭める）
        - `mid` は `True` 側で、答え候補なので**含めたい**
        - 右端は開区間なので `right = mid` で `mid` がそのまま含まれる（**+1 は不要**）
    - `left = mid + 1` の `+1` がないと、`mid == left` のとき区間が縮まらず無限ループになる
- 不等号で「lower / upper」が決まる（`bisect_left` vs `bisect_right`）
    - **lower_bound (`bisect_left`)**: `target` 以上の最小 index
        - 条件式: `if nums[mid] < target: left = mid + 1`（`<` を使う）
    - **upper_bound (`bisect_right`)**: `target` より大きい最小 index
        - 条件式: `if nums[mid] <= target: left = mid + 1`（`<=` を使う）
- `mid = left + (right - left) // 2` で書く理由
    - 数学的には `(left + right) // 2` と同値だが、C/Java など固定長整数の言語では `left + right` が**オーバーフローし得る**
    - Python では int が任意長なので問題ないが、慣習として揃えておくと安全か
- ループ不変条件で正しさを示す手順
    - **初期化**: 不変条件を満たす `i, j` が存在しないことを示す（vacuously true）
    - **維持**: 各分岐後にも不変条件が保たれることを示す（`nums` がソート済みであることを使う）
    - **終了**: `left == right` で抜けたとき、不変条件と合わせて「`left` が最初の `True` の位置」が言える
- 再帰でも書ける

</details>


<details>
<summary>153. Find Minimum in Rotated Sorted Array</summary>

- ループ不変条件を「`i < left` なら `nums[i]` 側は `False`、`i >= right` なら `nums[i]` 側は `True`」と置くと、終了時 `left == right` のとき「`True` になる最も左の index」が得られる
- このとき更新式は、`nums[middle]` が `False` 側なら `left = middle + 1` となる

</details>

<details>
<summary>33. Search in Rotated Sorted Array</summary>

- 評価関数の工夫

</details>


<details>
<summary>1011. Capacity To Ship Packages Within D Days</summary>

- 「条件を満たす最小値（最大値）」を求める問題であれば二分探索を適用できるかもしれない

</details>

<details>
<summary>50. Pow(x, n)</summary>

- 高速冪乗 (binary exponentiation)
    - 指数を2進展開し、立っているビットの位置だけ「累積二乗した底」を結果に掛け合わせれば O(log n) で計算できる
- `x ** 2` と `x * x` の違い
    - `**` は巨大値で `OverflowError` を投げ得るが、`*` はIEEE-754準拠で静かに `inf` を返す
    - `inf` は後段の演算でも一貫して伝播する（`inf * 有限 = inf`、`1/inf = 0.0`）ため、計算を止めずに済む
- IEEE-754 浮動小数点数の構成
    - 値の式: \( (-1)^{\text{符号}} \times 1.\text{仮数} \times 2^{\text{指数} - \text{bias}} \)
    - bias = \( 2^{(\text{指数部bit}) - 1} - 1 \)
    - 符号 / 指数 / 仮数 の bit 数
        - 単精度 (float):  32 bit = 1 / **8** / 23
        - 倍精度 (double): 64 bit = 1 / **11** / 52
    - 指数部の `8` と `11` を覚えておくと、復元
    - 特殊値: `1/0` が `inf`、`0/0` が `NaN` などもIEEE-754の規定
- Python の `int` と `float`
    - **`int` は任意精度 (arbitrary-precision / bignum)** で、ビット数の上限はない（メモリが許す限り桁を増やせる）
        - C/Java の `int32` / `int64` と違って算術オーバーフロー自体が起こらない
    - **`float` は IEEE-754 倍精度**に従うので上限・下限・精度の制約を受ける
        - Pow(x, n) は引数 `x` が `float` なので、ここの制約が効いてくる（int 同士なら問題にならなかった話）
    - Python 3.11 以降は DoS 対策で `int(s)` / `str(n)` の文字列⇔整数変換に既定 4300 桁の上限が入る
        - `sys.set_int_max_str_digits(0)` で解除できる
        - これは「整数の値そのもの」ではなく「文字列変換の桁数」に対する制限である
- 末尾再帰と Trampoline
    - `myPowHelper(base, exp, acc)` のように累積引数 `acc` を持たせれば末尾再帰の形に書ける
    - C/Scheme のような末尾再帰最適化 (TCO) があれば定数スタックで動くが、**Pythonは TCO を実装していない**ので、そのままだと深い再帰でスタック
        - <https://docs.python.org/3.15/whatsnew/3.14.html#whatsnew314-tail-call>
    - 代わりに **Trampoline** という手法でループへ展開できる
        - <https://note.com/_ikb_/n/nc67f3e541f20>
        - デコレータの内部で `nonlocal` の `firstcall` フラグと `params` を持ち、最初の呼び出しだけ `while` ループに入る。再帰呼び出しは引数だけ更新して即 `func` を返し、ループ側で次の反復として処理される
        - 結果として実際のスタック消費は定数になるが、関数呼び出しのオーバーヘッドが乗るため実行時間はやや遅くなる
- `functools.wraps`
    - デコレートした関数に元関数の `__name__` / `__doc__` などのメタデータを引き継がせる
    - <https://docs.python.org/ja/3/library/functools.html#functools.update_wrapper>
- 組み込み `pow` は3引数 `pow(base, exp, mod)` でモジュラー指数も計算できる（暗号系で使われる）
    - <https://docs.python.org/ja/3/library/functions.html#pow>

</details>

<details>
<summary>779. K-th Symbol in Grammar</summary>

- 出力は **n に依存しない**
    - 反復版を眺めると、操作は `half_length` で割っていくだけで、結果に効くのは flip の総数の偶奇のみ
    - つまり答えは「**`k - 1` の 2 進表記に立っている 1 の個数 (popcount) の偶奇**」
- 組み込み `int.bit_count()` で 1 行になる (`sol3.py`)
    - `(k - 1).bit_count() % 2`
    - <https://docs.python.org/ja/3/library/stdtypes.html#int.bit_count>
- ビット数を数える操作の用語整理
    - **Hamming weight**: ビット列に立っている 1 の個数。0 だけからなる文字列とのハミング距離と等価
    - **popcnt (Population Count)**: x86 などにあるハードウェア命令で、立っているビット数を 1 命令で数える
    - **SWAR (SIMD Within A Register)**: ハードウェア popcnt が無い環境でビット並列に popcount を計算する技法
        - シフトと `0x55555555` (`0101…`)、`0x33333333` (`0011…`)、`0x0F0F0F0F` (`00001111…`) などのマスクの AND を組み合わせ、2 bit ごと → 4 bit ごと → 8 bit ごと…と部分和を畳み込んでいく
        - 1 つのレジスタ内で複数の小さな並列加算を同時に進めるイメージ
    - **SIMD (Single Instruction, Multiple Data)**: 1 命令で複数データを同時処理する仕組み。日本語読みは「シムディー」
- GCC 10 / Clang 10 以降は、popcount 実装を自動でハードウェア `popcnt` 命令に置換してくれる
- 参考
    - <https://stackoverflow.com/questions/109023/count-the-number-of-set-bits-in-a-32-bit-integer#109025>

</details>
