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

<details>
<summary>108. Convert Sorted Array to Binary Search Tree</summary>

- ソート済み配列の中央を根にして、左右の半分から部分木を再帰的に作るのが一番素直
- スライス `nums[:idx]`, `nums[idx+1:]` で書くとシンプルだが、コピーが発生するため空間計算量がO(n log n)になる

</details>
