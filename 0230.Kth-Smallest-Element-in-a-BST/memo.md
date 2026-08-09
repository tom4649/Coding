# 230. Kth Smallest Element in a BST

## step1
in-orderで処理をすれば良い。再帰かループが考えられるが、まず解くことを目指して書きやすい再帰を選択。

11mぐらいで解けたが、nonlocalをつけずに一度間違えた。これは大きなミスだと思うので反省。変数のスコープは何度か確認したがまた間違えたので再度確認する。

### 変数のスコープ
PythonはLEGBルールに基づいて変数を探す。しかし、関数内に代入文があるとPythonはLocal変数であると解釈しEnclosingに変数を探しに行かなくなるため、nonlocal (またはglobal) 宣言が必要となる。mutableな変数の破壊的処理の場合にはnonlocalは不要。

> ある名前がコードブロック内のどこかで束縛操作されていたら、そのブロック内で使われるその名前はすべて、現在のブロックへの参照として扱われます。このため、ある名前がそのブロック内で束縛される前に使われるとエラーにつながります。この規則は敏感です。Python には宣言がなく、コードブロックのどこでも名前束縛操作ができます。あるコードブロックにおけるローカル変数は、ブロックのテキスト全体から名前束縛操作を走査することで決定されます。例は UnboundLocalError についての FAQ 項目 を参照してください。

https://docs.python.org/ja/3.11/reference/executionmodel.html#naming-and-binding

## step2

ループでも書く

> Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

わからないのでAIに聞いてみる：

真の最適解：「各ノードに、自分を根とする部分木の総ノード数（size）を持たせる（Augmented BST）」です。

データ構造を以下のように拡張します。

```python
class ImprovedTreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.size = 1  # 自分 ＋ 左部分木のノード数 ＋ 右部分木のノード数
```
sizeがあればこの問題は簡単になる。
sizeの変更はBSTの場合簡単なので、頻繁にinsertやdeleteが行われる場合に適していそう。
## 他の人のコード

https://github.com/thonda28/leetcode/pull/8

> インスタンス変数を使う場合はスレッドセーフでなくなる

ローカル変数であれば、スタック領域に変数が置かれるので、スレッドセーフである。

しかし、インスタンス変数の場合にはヒープに置かれるので、メモリ区間を共有するスレッドで共有される。

全く意識していなかったので勉強になった。

### スタックに積む書き方
こんな書き方もできるのか。

```python
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder_stack = []

        while True:
            while root:
                inorder_stack.append(root)
                root = root.left

            root = inorder_stack.pop()
            k -= 1
            if k == 0:
                return root.val

            root = root.right
```


C++でも書いてみる。ラムダ式を書けなかった。

auto 変数名 = [キャプチャ] (引数) -> 戻り値の型（省略可） {処理};

C++におけるラムダ式のは、関数に見えて実は「関数のように呼び出せる機能（operator()）を持った、名無しのインスタンス（オブジェクト）」
