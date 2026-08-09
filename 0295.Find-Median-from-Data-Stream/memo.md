# 295. Find Median from Data Stream

## step1

二分探索が真っ先に思いつきとりあえず書いてみると通った。
計算量を見積もると毎回O(n)。

## step2

solutionをチラ見してheapを使うことを見て書いた。heapを使うことを自力で思いつくようにならなければな。
heapqライブラリの使い方の確認になった。

時間計算量 O(logn)

> Find Median from Data Stream の RMQ BIT 平方分割

> データをビンソートし、中央値を求めることを考えました。ビンソートして中央値を求めるとき、 BIT または平方分割すると、 O(log n) や O(sqrt(n)) で求められるという話です。

分からないのでLLMに書かせてみる。要復習。

Binary Index Treeで区間の個数を持っておくのか。

#### 平方分割：

https://zenn.dev/student_blog/articles/72055eaeb62216

クエリをO(\sqrt{N})の計算量で処理できるため、配列全体を処理する (O(N)) よりも効率的

計算量的にはセグメント木がO(logN)より劣るが、実装がかなり簡単だ。複数クエリの問題で汎用性が高そう。

https://github.com/shining-ai/leetcode/pull/64

> https://docs.python.org/3/library/bisect.html#bisect.insort_left

bisect.insort_left、こんな便利な関数があるのか

若干早くなった

https://github.com/potrue/leetcode/pull/75

> 取り合えず入れてしまってからサイズを調整するアプローチ

これも書いてみる。プログラムの実行速度は若干遅くなる。挿入回数が増える場合があるため。

### step3

BITを書いたが短期記憶で書いている感じがする。新しい問題を見た時に適用できるようになるにはまだまだといった感じ。
