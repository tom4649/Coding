# 777. Swap Adjacent in LR String

## step1
最初 *.replace("X", "")を比較することを考えたが、L, Rの移動が一方に制限されているため誤り。

pointerでscanすることで解決。

## step2

https://leetcode.com/problems/swap-adjacent-in-lr-string/solutions/6970523/python-simple-two-pointers-by-rnotappl-yeij/?envType=problem-list-v2&envId=7p55wqm

同じ解法。ただし、こちらはwhileの条件が and でループの前にXの個数の一致を確認している。

これ以外の解法はない？

https://leetcode.com/problems/swap-adjacent-in-lr-string/solutions/2047353/python-on-with-comments-and-reasonings-b-kkw3/?envType=problem-list-v2&envId=7p55wqm
インデックスを全て保存する

## step3
TODO
