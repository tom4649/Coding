# 215. Kth Largest Element in an Array

## step1

heapを使った解法を思いつく。3minほど。

heappushpopを使った場合も書いた。

heapreplaceというメソッドもあるが今回は使わない。

## step2

Mediumとなっていることから考えて、本来の出題意図はQuick Selectを書かせたいのではないだろうか。

愚直に書くとTLEしたので、pivotの最初と終わりを返すようにした。

かなり時間がかかってしまった（測り忘れた）。添字と長さで混乱し、手で具体例を書いて添字を合わせた。

以下の問題のアルゴリズム（Dutch National Flag）に似ている。

https://leetcode.com/problems/sort-colors/description/?envType=problem-list-v2&envId=rab78cw1

Arai60の問題:

https://leetcode.com/problems/kth-largest-element-in-a-stream/description/

解くだけなら今回の問題の方が簡単だがQuick Selectを書くのが大変。

書き直したら分かりやすくなった。

## step3

Quick selectを書く。

間違えた点：

- left == rightの場合の処理（これがないと無限ループ）
- dutch flagのwhileの条件を<とした
