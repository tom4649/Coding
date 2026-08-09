# 875. Koko Eating Bananas

## step1
二分探索を思いつく。時間計算量はO(nlog max(piles))。17mほど。最小値と最大値を何度か間違えた（ガチャを引いてしまった）。

とりあえず書いた答えを残す。

改善する。

上限と下限を単純に 1, max(piles)とした方が可読性が上がるが、速度は落ちる。

## step2
二分探索を手で書く

https://leetcode.com/problems/koko-eating-bananas/solutions/7047251/simple-solution-by-harshita_114-3c0a/

can_eat_all の判定はfor文を使えば早期終了できる場合があるのか

実際の実行時間はジェネレータ表記の方が早かった

https://github.com/yamashita-ki/codingTest/pull/15

https://github.com/Exzrgs/LeetCode/pull/45/changes

https://github.com/TaisukeFujise/leetcode_tafujise/pull/16

## step3
今回は省略で良いだろう
