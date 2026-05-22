# 208. Implement Trie (Prefix Tree)

## step1

15mぐらい。自己流で実装したので一般的な実装かどうかは判断しかねる。

## 他の人のコード

https://github.com/huyfififi/coding-challenges/pull/35

is_endを持たせればwordを持たせる必要はない

> C++で書こうとしたが、メモリの解放を明示的に行う？か`unique_ptr`等の使用を検討しなければならなそうだったので、一旦このPRのスコープの範囲外とする

https://github.com/potrue/leetcode/pull/71

https://github.com/Kaichi-Irie/leetcode-python/pull/5

気が向いたら、サードパーティーライブラリーにどのような API があるのか、longest_prefix とか shortest_prefix とかを眺めておきましょう。
https://pygtrie.readthedocs.io/en/latest/index.html

`pygtrie` は Trie を dict っぽく扱えるライブラリ。LeetCode 208 では `insert` / `search` / `startsWith` だけを実装するが、実用上は「入力文字列に対して、登録済みキーのどれが prefix として一致するか」を調べる API が重要になる。

- `prefixes(key)`: `key` に向かって Trie をたどりながら、途中で値を持つノードをすべて返す。例えば登録済みキーが `foo` と `foo/bar/baz` のとき、`prefixes("foo/bar/baz/qux")` は `foo` と `foo/bar/baz` を返す。どちらも問い合わせ文字列 `foo/bar/baz/qux` の prefix になっているため。
- `longest_prefix(key)`: `prefixes(key)` の最後、つまり最も長く一致した登録済み prefix を返す。ルーティング、辞書の最長一致、IP プレフィックス検索のような用途に近い。
- `shortest_prefix(key)`: `prefixes(key)` の最初、つまり最も短く一致した登録済み prefix を返す。禁止語・除外パスなど、「どこかの prefix に引っかかったら十分」な用途で使えそう。

今回の `startsWith(prefix)` は「その prefix から始まる単語が Trie 内にあるか」を見る。一方で `longest_prefix(key)` などは「`key` の prefix になっている登録済み単語があるか」を見るので、探索の向きが少し違う。



## step2

is_endを採用。TrieNodeとTrieを分ける

以降型はOptionalよりTrie | Noneで書くことにしよう

Python 3.10で導入された

https://peps.python.org/pep-0604/

C++で書こうとしたが書けなかったのでLLMに協力を求めた。step3で書き直す。

26文字に限定されているのでdictよりもarrayの方が素直

メンバ変数には最後に_をつける

`std::unique_ptr<T>` は「ある `T` オブジェクトをただ 1 つの所有者として管理するスマートポインタ」。所有者である `unique_ptr` が破棄されると、持っているオブジェクトも自動で破棄される。

`std::make_unique<TrieNode>()` は、新しい `TrieNode` を作って、それを所有する `std::unique_ptr<TrieNode>` を返す関数。昔の C++ なら `new TrieNode()` のように書く場面だが、現代 C++ では `new` を直接書かずに `make_unique` を使うのが基本。

```cpp
std::unique_ptr<TrieNode> root_;

Trie() : root_(std::make_unique<TrieNode>()) {}
```

これは「`Trie` を作るとき、root 用の `TrieNode` を 1 個作り、`root_` に所有させる」という意味。

```cpp
Trie() { root_ = std::make_unique<TrieNode>(); }
```

でもこの例では最終的な状態はほぼ同じになる。ただし厳密には、初期化リストは `root_` を最初から `std::make_unique<TrieNode>()` の結果で初期化する。一方、コンストラクタ本体で代入する書き方は、先に `root_` が空の `unique_ptr` として初期化され、その後で新しい `TrieNode` を代入する。

そのため、メンバ変数の初期化は基本的に初期化リストで書く。`const` メンバ、参照メンバ、デフォルトコンストラクタを持たない型のメンバは、コンストラクタ本体での代入では初期化できない。

`Trie` が破棄されると `root_` も破棄され、root から `unique_ptr` でつながっている子ノードも連鎖的に解放される。

## step3

C++の習得は道のりが長そう
