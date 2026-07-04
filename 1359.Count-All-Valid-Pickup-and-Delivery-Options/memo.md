# 1359. Count All Valid Pickup and Delivery Options

## step1
算数だと思って解いた。9mほど。

modulo定数はSolution固有だと考えてクラス内に定義する。グローバル変数にしても良いと思う。

バックトラックがキーワードにあるので書くがTLEした。他の書き方があるのか？

## 他の解法
https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/solutions/4024280/9957-dp-math-recursion-by-vanamsen-qd4r/

再帰と直接計算する方法

https://docs.python.org/ja/3/library/functions.html#pow

> If mod is present and exp is negative, base must be relatively prime to mod. In that case, pow(inv_base, -exp, mod) is returned, where inv_base is an inverse to base modulo mod.

逆元の計算をpowで行える

https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/solutions/3223439/2-python-solutions-with-explanation-using-dp-and-backtracking/

バックトラックはほとんど自分と同じ解法なので、TLEを避ける方法はなさそう？

https://discord.com/channels/1084280443945353267/1196498607977799853/1358454829005144125

>  Count All Valid Pickup and Delivery Options ... Math・Dynamic Programming・Combinatorics に分類される問題に、ソフトウェアエンジニアとしての教育効果がどれくらいあるのか分かりませんでした。最近の入社試験で出題されるということであり、かつ入社試験に向けた練習をするのであれば、入れたほうがよいと思います。

## step3
省略
