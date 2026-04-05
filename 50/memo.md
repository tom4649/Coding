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

「指数を半分にしつつ、底を毎回 x**2 に置き換える」やりかただとオーバーフローが生じたので、底を変えない形にした。

追記：
これは x`*`xとすれば解決する。`**`演算だとエラーを投げますが、*演算だとinfを返すためである。


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


追記：
helper 関数を用いる場合を追記
このhelper関数は末尾再帰最適化を行うことで真価が発揮される。
しかし、pythonではこれが行われないらしく、追加の処理が必要になる
(末尾再帰最適化が実装されていないこと)
https://docs.python.org/3.15/whatsnew/3.14.html#whatsnew314-tail-call

しかし、Pythonは末尾再帰最適化を実装しておらず、これにはTrampolineという手法を用いるのが良いらしい。
自分で実装してみる
https://note.com/_ikb_/n/nc67f3e541f20


Geminiや記事を参考に自分なりに言語化すると、
最初に末尾再帰関数が呼ばれるとfirstcall=Trueなのでwhile文に入る。
nonlocalを使用しているため、tail_recursiveのlocal変数は全ての呼び出しで共通である。
そこで次の関数が呼ばれるがすでにfirstcall=Falseになっているので、引数だけを更新してfuncを返し、すぐに終了する。
これが続いて引数を更新し続け、最後に値が返ってwhileを抜ける。

実際にスタックのメモリ使用量に差が出ることを確認できた。
なお、実行時間はやや遅くなる

functools.wrapper
関数のメタデータを新しい関数に引き継ぐ

https://docs.python.org/ja/3/library/functools.html#functools.update_wrapper
