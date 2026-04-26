# 323. Number of Connected Components in an Undirected Graph

https://neetcode.io/problems/count-connected-components/question

UnionFindを（不備があったが）空でかけた: sol1.py

調べて改善: sol2.py
rankとcountを持たせる。findのときに経路圧縮を行う。unionのときにもランクを考慮する。


### 他の人のコード

https://github.com/naoto-iwase/leetcode/pull/28/changes

Unionfindのまとめがわかりやすい

https://github.com/mamo3gr/arai60/blob/323_number-of-connected-components-in-an-undirected-graph/323_number-of-connected-components-in-an-undirected-graph/memo.md

DFSでも解けるのか
自分でも書いてみる: sol3.py
