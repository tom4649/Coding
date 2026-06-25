# 19. Remove Nth Node From End of List

## step1
一巡して長さを求めて、もう一巡して削除を行う。8mぐらい。今回はミスがなかった。

削除したNodeのnextをNoneに変更した。メモリリークを明示的に防ぐためである。

制約も小さく、解くだけなら簡単な問題なので、他の方針も考える。

> Follow up: Could you do this in one pass?

hashmapを使えば実現できる

nth がendから数えたものなので、一度最後まで走査しないと削除が実行できない。これ以外の方針は思いつかない。

## 他の人のコード

https://github.com/thonda28/leetcode/pull/18

slowとfastを使うのか、なるほど。自分で思いつきたいところだった。

> step1のslow, fastの方が(個人的には)読みやすく感じました


このコードでは上述のメモリリークの対策はしていないようだが、した方が良いように思う

## step2
