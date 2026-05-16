# 733. Flood Fill

## step1
in-placeだが良いだろう

DFS

## step2

他の人のコード

https://github.com/huyfififi/coding-challenges/pull/9

- キュー／スタックに入れる前に色を塗る／範囲を先に見ることで重複探索を防ぐ（DFS で「呼び出し後に塗る」と無限再帰になりうる）

https://github.com/ryosuketc/leetcode_grind75/pull/9

https://github.com/Kitaken0107/GrindEasy/pull/12


同じBFS/DFSでもキューに入れる前に条件で省くか、とりあえず入れておくかの二通りがある。

個人的には無駄な操作を省く前者の方が好み

読みやすさ的には後者を好む人もいそう






> 3回passするようになると、コードがちょうどいい抽象度で頭に収まるような実感がある。

サボっているので真面目にやるべきなのか...

seenが不要なのでその点を改良する

## step3

個人的に馴染みのない、BFS+とりあえず入れておく解法を書く
