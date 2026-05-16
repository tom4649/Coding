# 543. Diameter of Binary Tree

## step1

15mぐらいかかった

DFSでdepthを返しつつdiameterを更新していく方針

### Python のスコープと `nonlocal`

参考:
- https://docs.python.org/3/reference/executionmodel.html#resolution-of-names
- https://docs.python.org/3/reference/simple_stmts.html#the-nonlocal-statement
- https://docs.python.org/3/reference/simple_stmts.html#the-global-statement

Python では、関数内である名前に代入すると、その名前はデフォルトでその関数のローカル変数として扱われる。

```python
def outer():
    diameter = 0

    def dfs(node):
        # nonlocal がないと、diameter は dfs のローカル変数扱いになる
        diameter = max(diameter, 1)
```

この場合、右辺の `diameter` も `dfs` のローカル変数として読もうとするが、まだ値が入っていないため `UnboundLocalError` になる。

外側の関数スコープにある変数へ再代入したい場合は `nonlocal` を使う。

```python
def outer():
    diameter = 0

    def dfs(node):
        nonlocal diameter
        diameter = max(diameter, 1)
```

参照するだけなら `nonlocal` は不要。

```python
def outer():
    diameter = 0

    def dfs(node):
        return diameter
```

ミュータブルなオブジェクトの中身を変更するだけでも `nonlocal` は不要。変数名そのものへ再代入していないため。

```python
def outer():
    values = []

    def dfs(node):
        values.append(1)
```

ただし、同じ `values` という名前に新しいリストを代入するなら `nonlocal` が必要。

```python
def outer():
    values = []

    def dfs(node):
        nonlocal values
        values = [1]
```

`global` は外側の関数ではなく、モジュールスコープの変数を指す。

```python
x = 0

def f():
    global x
    x = 1
```

名前解決のざっくりした順序は LEGB。

- Local: 今の関数内
- Enclosing: 外側の関数内
- Global: モジュール内
- Built-in: `len` などの組み込み

`nonlocal` は Enclosing の名前を使う宣言で、`global` は Global の名前を使う宣言。


## step2

>関数名について。
>GetHeight は、名前として、中身を見ていないと高さが返ってくると思いますね。あと、-1 が返るというのも、名前からはびっくり度が高いです。
>
>だいたい選択肢は3つで
>isBalancedAuxiliary など補助関数で呼ぶことがまったく想定されていないような名前にする。
>pair<int, bool> get_height_and_is_balanced(TreeNode* root) のようにペアを返す。
>int get_height(TreeNode* root, bool* is_balanced) という風にポインターにバランスしているかを書き込む。

関数名と返り値の意味がずれていると読み手が驚く。
例えば `GetHeight` という名前なのに、木が balanced でない場合に `-1` を返す実装だと、名前から期待する「高さを返す関数」と実際の「高さまたはエラー値を返す関数」がずれている。

こういう場合の選択肢は大きく次の3つ。

自分の `step1.py` では、`depth_of` は深さを返すだけでなく、`nonlocal diameter` を更新する副作用も持っているので指摘があてはまるかも

改善するなら、例えば `compute_depth_and_update_diameter` のように副作用を名前に含めるか、`depth_of` のままにして直前に「深さを返しつつ diameter を更新する」とコメントを書くと読み手の驚きが減る。

https://github.com/Kitaken0107/GrindEasy/pull/17#discussion_r1616234817

参照透過性

https://ja.wikipedia.org/wiki/%E5%8F%82%E7%85%A7%E9%80%8F%E9%81%8E%E6%80%A7

- 参照透過性
  - 参照透過性は、同じ入力に対して同じ結果を返し、式をその値で置き換えてもプログラムの意味が変わらない性質
  - `self.diameter` のように外部状態を持つと、同じ `root` を渡しても「その前に何を呼んだか」によって結果が変わる可能性がある。この場合、関数の結果が引数だけで決まらない
  - 今回のような単純な関数では、状態をインスタンスに残すメリットが少ないため、返り値で必要な情報を返す方が扱いやすい

- 解法
  - 最初の解法は `self.diameter` をインスタンス変数として持ち、DFS の中で高さを返しながら `self.diameter = max(self.diameter, left + right)` で直径を更新する
  - この方針は自分の `step1.py` の `nonlocal diameter` とほぼ同じで、「返り値は高さ」「外側の状態に直径を保存」という形
  - 改善版では `calculate_diameter_height(node)` が `(diameter, height)` のペアを返す。左部分木・右部分木の直径と、`left_height + right_height` の最大を現在の直径として返す




https://github.com/naoto-iwase/leetcode/pull/71

- 解法
  - 再帰版では、各ノードについて `(diameter, depth)` を返す。左部分木の直径、右部分木の直径、そのノードを通る `left_depth + right_depth` の最大が現在の直径
  - iterative 版では、再帰の帰りがけ処理を stack で再現している。子から親への引き継ぎ用に空リストを置き、非空になったら処理済みとみなす
  - `None` は `(0, 0)` を返す扱いにすることで、葉の高さや直径の計算を統一している


https://github.com/ryosuketc/leetcode_grind75/pull/21

https://github.com/huyfififi/coding-challenges/pull/21

- 最初に「root の左部分木の高さ + 右部分木の高さ」と考えたが、直径が root を通らないケースに気づいて修正している。これは自分も最初間違えた。
- レビュー
  - post-order の iterative 実装は、行きがけと帰りがけで処理が違うため、pre-order 系の問題より複雑になる
  - 型ヒントは複雑な構造に律儀につけると、逆に読みづらくなることがある
  - `Optional[A]` より `A | None` の方が現在の Python では読みやすい場合がある。ただし LeetCode の雛形に合わせる選択もある
  - 補助関数名の `calculate_*` は「計算している」というより「探索しながら集約している」ので違和感がある、というレビュー
  - `get_*` は軽量 accessor の印象があるため、木全体を走査する `O(n)` の処理にはあまり合わない


naoto-iwase さんのIterative を真似して書いておく。

DFSではfrontierよりstackの名前の方が適切に思われるの今後はそのようにしようと思う。


