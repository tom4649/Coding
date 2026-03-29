# 139. Word Break

sol1.py: 時間制限に引っかかる。このコード以外にも複数ためしたが、wordDictを全探索して削るやり方だとうまくいかない
再帰関数を定義し、メモ化するようにしたらうまくいった

https://discord.com/channels/1084280443945353267/1200089668901937312/1222092873508323368

> 0文字目から開始して、len(s)文字目に到達できれば受理します。

結局DFSで解けるのか。削除した文字列は数字で管理すれば良い。

> この問題、まず正規表現で書くことができるので O(n) で解けるはずとまず初めに考えました。
> ((apple)|(pen))*
> 次に、その場合のよくある話として
> "a" * 51
> は、
> "a" * 2 と "a" * 4 で表せないので、単純なバックトラックでは失敗するというのが予想です。

「正規表現で書けるからO(n)」はあくまでwordDictが定数のときの話だろう。ただこの考えは持っておきたい。

> というわけで、先頭から DP が"模範解答"だろうな、とは思います。

> たとえば、priority queue を用意して、そこに数字 N が入っている場合は「先頭から N 文字目までの部分文字列は、wordDict の結合で表現できる」ということを意味する、とかします。
> 初期値は [0] (0文字目までは表現できる。)ですね。



https://github.com/garunitule/coding_practice/pull/39

トライ木を使った実装

dataclass
https://docs.python.org/ja/3.10/library/dataclasses.html

https://docs.python.org/3.10/library/dataclasses.html#dataclasses.field

> default_factory: If provided, it must be a zero-argument callable that will be called when a default value is needed for this field. Among other purposes, this can be used to specify fields with mutable default values, as discussed below. It is an error to specify both default and default_factory.

> This has the same issue as the original example using class C. That is, two instances of class D that do not specify a value for x when creating a class instance will share the same copy of x. Because dataclasses just use normal Python class creation they also share this behavior. There is no general way for Data Classes to detect this condition. Instead, the dataclass() decorator will raise a TypeError if it detects a default parameter of type list, dict, or set. This is a partial solution, but it does protect against many common errors.

> Using default factory functions is a way to create new instances of mutable types as default values for fields:

つまり、mutableな型を、クラス変数として置いたり、dataclass のフィールドのデフォルト値に直接書いたりするとインスタンス間で共有されてしまうことがある。dataclass も通常のPythonのクラス生成の仕組みに従うため基本的に同じだが、list/dict/set をデフォルトに直接指定した場合はTypeErrorを出して事故を減らす。default_factory を使えば、インスタンス生成のたびに新しいmutableを作って各インスタンスに持たせられる。


https://github.com/mamo3gr/arai60/blob/139_word-break/139_word-break/step3_tuple_words.py

> str.startswithがtuple[str]を受け取れる

知らなかった。直感的にわかりやすい。


計算量
n = |s|, m = len(wordDict), l = max([len(word) for word in wordDoct])とする

sol1.py
時間 O(nml): can_breakはメモ化しているので高々O(n)回呼び出される、それぞれの関数内でwordDict内全ての文字列比較をするので O(ml)
空間 O(n): 再帰スタックとメモ化

sol2.py
時間 O(nml): (visitedを使っているので)各単語の訪問回数は高々一回 O(n)、それぞれwordDictを全走査O(m)、文字列比較 O(l)
空間 O(n)：visited, frontierの管理

sol3.py
時間 O((m+n)l): Trie木の構築 O(ml)、can_reachが全てTrueになった場合の探索 O(nl)
空間 O(ml+n): Trie木 O(ml)、can_reach O(n)

sol2.pyは位置それぞれで文字列比較を行う分時間計算量が大きい。

sol2, sol3は自分で思いつけていないので後でやり直したい
