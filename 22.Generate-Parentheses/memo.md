# 22.Generate Parentheses

最初にDFSを思いついたので解く: sol1.py

バックトラック: sol2.py

### コメント集
> Python での計算時間の見積もり方。ネイティブコードで走るか否か。

joinはCPythonで書かれているんだった

> 計算量はあくまでも極限での振る舞いなので、計算量を使って計算時間を見積もるのが大事です。

> また、速度が速いかどうかは、普通コーディングにおいてそれほどプライオリティーが高くないです。

> Generator をキャッシュする方法についてのコメント。

Generatorをキャッシュするデコレータを作ろうとしたけど、kargsがキーの挿入順に依存してしまっている

https://github.com/olsen-blue/Arai60/pull/54#discussion_r2027288220

> これは解の空間をどう分けるか、分類するかの考え方で網羅的に分類できていればなんでもいいのです。

分類の網羅、は覚えておこう

https://github.com/hroc135/leetcode/pull/50#discussion_r2052246310


高階関数

https://github.com/fuga-98/arai60/pull/52#discussion_r2137961581
> 文字列を丸ごとコピーしないようにするやつを、Python にしてみました。

https://github.com/hroc135/leetcode/pull/50

strings.Builderに書き込む関数を再帰で組み合わせている
再帰は関数の合成、ということだろうか
文字列のコピーがないので高速
自分では書けそうにないが




https://github.com/olsen-blue/Arai60/pull/54#discussion_r2027288220

これは面白い解法だ。なるほど、最初の左かっこに対応する右かっこの位置で場合分けをしている: sol3.py
- メモ化再帰に直した

### 追記
sol2 と sol2_revisedを比較すると速さはそれほど変わらない、というかrevisedの方が少し遅かった（geminiに手伝ってもらいました）

答えの本数だけlistからjoinでstrに毎回変換し、文字列の更新よりもオーバヘッドが大きいためだと考えられる

-----------------------------------------------------------
n= 8  number= 5  sol2:     8.40 ms  sol2_revised:    10.00 ms  (revised / sol2 = 1.190)
n=10  number= 5  sol2:   103.18 ms  sol2_revised:   116.89 ms  (revised / sol2 = 1.133)
n=12  number= 2  sol2:   520.99 ms  sol2_revised:   594.95 ms  (revised / sol2 = 1.142)
n=13  number= 1  sol2:   933.25 ms  sol2_revised:  1076.60 ms  (revised / sol2 = 1.154)
