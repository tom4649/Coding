# 297. Serialize and Deserialize Binary Tree

## step1

37mぐらいかかった。確実に解けると思ったが、スラスラと書くことができなかった。

幅優先探索で解くことにした。

間違えた点：
- delimをつけずに間違えた(数字が2桁だとdecodeできない)
- deserializeでキューになぜかNoneを入れた


## step2

https://support.leetcode.com/hc/en-us/articles/32442719377939-How-to-create-test-cases-on-LeetCode#h_01J5EGREAW3NAEJ14XC07GRW1A

こんなサイトがあることを知らなかった。level order traversalという名前がついていたんだった。

探索順は同じだが、serializeした文字列がこちらの方が短い。nullの場合の処理が異なる。

この場合、自身をresultに入れてから、子をresultに入れるとかける: step2

こちらも書くのに20mぐらいかかった。

書きながら注意したことで、以下は正しく動かない。

```python
child = node.left
child = TreeNode(0)
```

これはPythonの変数がオブジェクトの参照であるためで、childが単に`TreeNode(0)`オブジェクトを指すようになる、という変更になる。

## 他の解法

LeetCodeの与えられ方に引きずられて、level-orderを最初に選択したが、DFSでも解くことができるはず。

11mぐらいでかけた。

Pre-orderとPost-orderは可能だが、In-orderは可能なのか？おそらく不可能だと思う。理由は、in-orderだとnull Nodeがある場合に根の位置が特定できないから。


LeetCodeのSolutionを検索すると in-order と書かれているものがあったが、コードを読むと実際にはpre-orderであった。
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/solutions/6678162/in-order-traversal-simple-solution-by-th-822j/?envType=problem-list-v2&envId=rab78cw1



## 他の人のコード

https://github.com/hayashi-ay/leetcode/pull/74

> 書いてみた感想として、探索だけならDFSもBFSもそこまで書きやすさは変わらないですが、Treeの構築が発生する場合はBFSおよびDFSのループだと書きにくいなと思いました。親ノードや左右どちらにつなぐかなどを考えないといけないので。

確かに自分もBFSで書くので苦戦し、再帰DFSで書くと簡単にかけた

自分はindexを使ったが、iteratorを使っている。例外で処理しようとしたが、nextの引数defaultを勧められている。nextの引数defaultは知らなかった。

https://docs.python.org/3/library/functions.html#next

https://github.com/shining-ai/leetcode/pull/62

> イテレータを使う発想がありませんでした。

自分も同じく。

https://github.com/potrue/leetcode/pull/73


