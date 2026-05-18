# 75. Sort Colors

## step1
まず2回走査のアルゴリズムはすぐにかける。他の問題で見た気がする。5mぐらい。

> Follow up: Could you come up with a one-pass algorithm using only constant extra space?

値が三種類だけというのを利用すれば可能。

方針が立ったが、実装に時間がかかった。 2 を後ろにおくった時にまえに送られる値が 2 である可能性を考慮し忘れていた。15 mぐらい。

## step2
変数名を書き直したが、どうだろうか

### 他の人のコード

https://github.com/huyfififi/coding-challenges/pull/49

レビューにあるzero, one, twoのポインタを使う実装がわかりやすかったので実装

4色以上の場合の実装も行う。自力でこれを一から書ける気がしない。

### in-place のソートアルゴリズム

Bubble sort: https://en.wikipedia.org/wiki/Bubble_sort

> It performs poorly in real-world use and is used primarily as an educational tool.
> Like insertion sort, bubble sort is adaptive, which can give it an advantage over algorithms like quicksort. This means that it may outperform those algorithms in cases where the list is already mostly sorted (having a small number of inversions), despite the fact that it has worse average-case time complexity. For example, bubble sort is O ( n ) {\displaystyle O(n)} on a list that is already sorted, while quicksort would still perform its entire O ( n log ⁡ n ) {\displaystyle O(n\log n)} sorting process.

Insertion sort: https://en.wikipedia.org/wiki/Insertion_sort

> Adaptive, i.e., efficient for data sets that are already substantially sorted: the time complexity is O(kn) when each element in the input is no more than k places away from its sorted position
> Stable; i.e., does not change the relative order of elements with equal keys
> In-place; i.e., only requires a constant amount O(1) of additional memory space

Selection sort: https://en.wikipedia.org/wiki/Selection_sort

> Heapsort has been described as "nothing but an implementation of selection sort using the right data structure."

バブルソートより計算量が少ない。（工夫しないと）安定ソートではない。

ヒープソートもin-placeで実装できる

