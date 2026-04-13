# 779. K-th Symbol in Grammar

紙に書いて考えてみると、問題の条件は

1. 前半分の文字列は前の行の文字列
2. 後半分の文字列は前半分の文字列のflip
3. 最初(n=1)が0

で特徴づけられることに気が付く。（おそらく同値だと思う）

これを用いて再帰を書く: sol1.py

再帰を使わずに書く場合も考える: sol2.py

## コメント集

https://discord.com/channels/1084280443945353267/1200089668901937312/1216054396161622078

> 実は、ビットの数を調べるのは、たまに大事で、有名なアルゴリズムがあります。

> ビット演算だけでできる計算って実はかなり豊かなんですよね。

https://stackoverflow.com/questions/109023/count-the-number-of-set-bits-in-a-32-bit-integer#109025
これを読んでみる

二進表現で 1 が立っているビットの個数（Hamming weight / population count / popcount）を数えるアルゴリズムについての議論

- CPU次第で一番速いのは違う
- GCC 10 / Clang 10 以降は、ハードウェアの popcount に置き換えられる
- SWARアルゴリズム
```
i = i - ((i >> 1) & 0x55555555); # (i & 0x55555555) + ((i >> 1) & 0x55555555)に等しい。0x55555555は1010...101なので偶数ビットと基数ビットを足している
i = (i & 0x33333333) + ((i >> 2) & 0x33333333); #二ビットごとの {0, 1, 2} の和を4ビットごとに {0, 1, 2, 3, 4}の和にまとめる
i = (i + (i >> 4)) & 0x0F0F0F0F; 同様に4ビットごとの和を8ビットにまとめる

i *= 0x01010101; # i + (i<<8) + (i<<16) + (i<<24)に等しい。最上位の8ビットにまとめる
return i >> 24; # まとめた和を取り出す
```



https://github.com/hayashi-ay/leetcode/pull/46

> 出力は n　の値に依存しません。その点を考慮し、もう少し効率の良い回答を考えてみても良いかもしれません。ただ、そこまで踏み込むと、ただの数学パズルのため、踏み込まなくても良いかもしれません。

たしかに sol2.pyの操作は n に依存しない。さらに最後に１が余る性質を利用すれば1を引いてから考えれば良いのか

組み込み関数 int.bit_countを使う
https://docs.python.org/ja/3/library/stdtypes.html#int.bit_count


https://github.com/hroc135/leetcode/pull/44/changes/BASE..caccade39f42ccaeac9b6b2e5d981ace708ffc3b#diff-51246bfe90de9312497a14a935a13980cce9e8a58b9614c7d17f48d8ac78129a

最後のメモが参考になった
