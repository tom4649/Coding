# 50. Pow(x, n)

https://leetcode.com/problems/powx-n/

sol1.pyを迷わずかけた。n<0のケースでエラーが出たが、絶対値を取ることで処理し、それ以外ではつまらなかった。冪乗と聞いてビット演算を用いることを思いついた。

実行時間は0ms

計算量は時間計算量 O(log(n)) 、空間計算量 O(1)


> 1/2 乗って要するにルートのことですよね。

https://discord.com/channels/1084280443945353267/1262688866326941718/1351739946360111126

https://github.com/hroc135/leetcode/pull/43/changes#diff-788d4e4d3d8fc9d0d4ea879b815deba3b2c21e39a44274fe799eaa496c5d2e43

組み込み関数のコードを読んでいる

pythonのpowのドキュメント

https://docs.python.org/ja/3/library/functions.html#pow

powがmodの引数を取れることは知らなかった

https://github.com/TORUS0818/leetcode/pull/47/changes
再帰で書く

ループがかければ再帰は簡単に書けるように思う。
再帰をはじめに思いついたときにループに直せるようにしておきたい。

sol2.pyを再帰でかいた。

「指数を半分にしつつ、底を毎回 x**2 に置き換える」やりかただとオーバーフローが生じたので、底を変えない形にした


> IEEE-754の内部ビットの数も覚えておくと、面接でよく分かっている風が醸せることがあります。
> exponent が8ビットと11ビットです。符号が1ビットで残りが23ビットと52ビットです。

https://github.com/hroc135/leetcode/pull/43#discussion_r2002298814

(-1)^{符号} * 1.{仮数} * 2**{指数-bias}
bias = 2^{指数部のbit} -1

符号/指数/仮数

単精度 (float)	32 bits	1 / 8 / 23
倍精度 (double)	64 bits	1 / 11 / 52

指数部の8と11だけ覚えれば良い

この辺りの知識、頭から抜けてしまっているので復習したい



