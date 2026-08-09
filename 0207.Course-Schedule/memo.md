# 207. Course Schedule

## step1

DAG判定だと思う。トポロジカルソート。

step1_loop.pyを10mで書いたが遅い。おそらく set の再構築に時間がかかっているのだろう。

step1_backtrack.pyにすると多少速くなった。

ただ空間計算量が O(V^2)

## step2

### 他の人のコード

https://github.com/huyfififi/coding-challenges/pull/34

> NOT_VISITED_YET = 0
> VISITING = 1
> VISITED = 2

これを使って書き直すと、loopの方で速度がBeats 100%となった。

> トポロジカルソートの中でも特にKahn's algorithmと呼ばれるもの

https://ja.wikipedia.org/wiki/%E3%83%88%E3%83%9D%E3%83%AD%E3%82%B8%E3%82%AB%E3%83%AB%E3%82%BD%E3%83%BC%E3%83%88

これを実装。個人的にはqueueを使わないもののほうがわかりやすい。

https://github.com/potrue/leetcode/pull/76

https://github.com/thonda28/leetcode/pull/3

https://github.com/thonda28/leetcode/pull/3
