# 235. Lowest Common Ancestor of a Binary Search Tree

## step1

root: 'TreeNode'

16mぐらい。BFSで探索し、親ノードを残しておく。

元のコードにあった型をクォーテーションで囲むのは前方参照を解決するための、`from __future__ import annotation`以前の方法。TreeNodeのメソッドとして書くことを想定したのだろうか？

binary **search** treeであったことに解き終わってから気がついた。valを探索に使うことができる。そうなると「二つのvalの間にある、深さ最小のノード」が答えとなる

## 他の人のコードなど

> Unreachable なところに raise を書くことですが、ありかもしれませんが、私はそこまで肯定的ではないです。結構微妙なところだと思います。

> まず、一般的に、dead code は避けるものです。
> また、Python の場合、返り値があって到達する場合はあってもなくても同じだが return None を書き、到達しない場合は書かないことで、unreachable かの意図は表現されるはずです。

書かない方が望ましいようだ。

https://github.com/naoto-iwase/leetcode/pull/66

- 3つ以上に一般化するなあどかなり工夫されている
- lower, upper = sorted([p.val, q.val]) の書き方
- p, q自体を交換するよりわかりやすいかも。
- pathを保存しているが、自分のparentのみ保存でも良きがする



- コメント

```python
if lower <= node.val <= upper:
    return node
```
を一番初めに持ってきたほうが明確ではないですかね。

- p または q が見つかった場合にはそれを返し、見つからなかった場合には None を返すようなコードで再帰的に処理するイメージです。

「root以下にあるp, qのLCAを返す」アルゴリズム。ボトムアップ再帰。

```python
class Solution:
    def lowestCommonAncestor(
        self,
        root: TreeNode,
        p: TreeNode,
        q: TreeNode
    ) -> Optional[TreeNode]:
        if root == p or root == q:
            return root

        left = None
        if root.left:
            left = self.lowestCommonAncestor(root.left, p, q)

        right = None
        if root.right:
            right = self.lowestCommonAncestor(root.right, p, q)

        # 左右両方で見つかれば root が LCA
        if left and right:
            return root

        # 片方だけ見つかった場合、見つかった方を返す
        return left if left else right
```

https://github.com/ryosuketc/leetcode_grind75/pull/10

https://github.com/huyfififi/coding-challenges/pull/10

step1_1.pyは上のボトムアップ再帰になっている。

> よく考えたら、せっかくBinary Search Treeが与えられているのに、その性質を利用していなかった。

問題文を読んだ時の誤解が自分だけではなかったのは少し安心

## C++
今回は難しいコードではないので動くものは書けた。
