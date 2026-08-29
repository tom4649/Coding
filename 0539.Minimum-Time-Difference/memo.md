# 539. Minimum Time Difference

## step1
ソートする解法はすぐに思いつく。10m。日をまたぐ差分を考慮せずに一度間違えた。
計算量O(nlogn)

## step2
変数名を改善。

https://leetcode.com/problems/minimum-time-difference/editorial/?envType=problem-list-v2&envId=7p55wqm

バケットソート。全く思いつかなかった。ソート対象の値が限られているときにバケットソートが使えることを覚えておきたい。
計算量 O(1)

## step3

sortedcontainers.SortedList: 検索、追加、削除が 平均O(logN)で可能なデータ構造（最悪はO(N)）

一定サイズに分割した二重配列_lists、部分配列の最大値を格納した_maxes、要素数を木構造で管理する_index で管理している

https://grantjenks.com/docs/sortedcontainers/introduction.html

https://github.com/grantjenks/python-sortedcontainers/tree/master/src/sortedcontainers
