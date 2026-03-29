# 121. Best Time to Buy and Sell Stock

- sol1.py: 配列を逆向きにたどり、将来の最大値を覚えておきながら、その日買ったときの利益を計算する
- sol2.py: 配列を順にたどり、過去の最小値を覚えておきながら、その日に売ったときの利益を計算する

https://discord.com/channels/1084280443945353267/1206101582861697046/1219181674038820945
> prices が空の場合は、何を返すことが想定されているでしょうか。

考えていなかったな

> Haskell だと、scanl scanl1 の二つの関数があります。scanl1 は、リストの先頭を初期値として与えます。
> つまり、scanl1 min prices というのが、そこまでの最小値のリストを返します。

https://discord.com/channels/1084280443945353267/1196472827457589338/1196473519689703444
> 本質的には、
> scanl min でその日までの最安の値。
> zipWith (-) で利益。
> max を取る。

https://github.com/mamo3gr/arai60/blob/121_best-time-to-buy-and-sell-stock/121_best-time-to-buy-and-sell-stock/memo.md
step1: 解法はほぼ同じだが、初期値をlistの先頭としている + コーナーケースを場合分け
step2: 上のHaskelのコードをpythonに直したもの。itertools.accumulateを使う
https://docs.python.org/ja/3/library/itertools.html#itertools.accumulate
- sol3.py

https://github.com/naoto-iwase/leetcode/pull/42
> どのスタイルに準拠するかによりますが、たとえば Google では import itertools -> itertools.islice といった使い方をします。
> Use import statements for packages and modules only, not for individual types, classes, or functions.

> Python 3.9 以降は built-in list を使うことになっています。

https://docs.python.org/3/library/typing.html#typing.List

https://docs.python.org/3/library/typing.html#typing.List

> Note that to annotate arguments, it is preferred to use an abstract collection type such as Sequence or Iterable rather than to use list or typing.List.

> これは list 以外でもそうですが、引数の type hint はより abstract に、返り値はより specific にすることが多いかと思います。

色々知らなかった

> 別の考え方として、「買う前の状態」「株を持っている状態」「売った状態」の3状態しかないので、それぞれの状態での最大の所持金(スタートを0とする)を考えるというのもあります。

なるほど、同じコードでも解釈を変えることができるのか
