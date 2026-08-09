# 148. Sort List

## step1
22mかかった。先頭からスキャンするListNodeの性質上、マージソートが良いだろう。

関数mergeの最後でhead.next = Noneをつけずにメモリエラーが生じた。これは答えの確認時に起きたのではないかと思われる。

空間計算量が O(log n)

## step2
https://github.com/potrue/leetcode/pull/69

再帰を使わずにマージを行っている。なるほど。

確かにlistに値を格納してしまえば標準ライブラリが使えるけど問題の意図を汲んでいない気がする。

> Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

上の解法がこの答えになっている

リストをカットしないものを書く

## step3
TODO
