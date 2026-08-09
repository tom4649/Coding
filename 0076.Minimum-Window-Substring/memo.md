# 76. Minimum Window Substring

## step1
32mほどで解いた。sliding windowを使えばO(n)で解けることにはすぐに気がついたが、処理をコードに変換するのに時間がかかった。最初の解法: step1.py

おそらくこの問題の解法は sliding window を用いた用いたこの解法しかないのでは。あとは同じ解法で以下にコードを改善するか。


## 他の人のコード
https://github.com/hayashi-ay/leetcode/pull/73

> 工夫すると毎回全ての文字のカウントを確認しなくて済むような方法があります。

たしかに最も単純なのは毎回全ての文字のカウントを確認する方法になるのか。

変数名はleft, rightがわかりやすい。
書き方はright の for 文で回した方がわかりやすいな

https://github.com/shining-ai/leetcode/pull/61
条件を num_matches で管理するのはわかりやすい

他に ord を用いて配列をdictの代わりに用いる方法がある

https://github.com/potrue/leetcode/pull/67/changes

## step2
for 文で書き直す。他に、クラスを使ってwindow_infoを定義する工夫をした（大袈裟かもしれない）。

## step3
書く

