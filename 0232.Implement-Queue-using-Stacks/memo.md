# 232. Implement Queue using Stacks

## step1
Stackを二つ使えという指示がヒントになりそう

計算量O(1)の方法が思いつかず悩む。そもそもO(1)の答えが期待されているのか？

Follow-upを見るとamortizeでO(1)であれば良いらしい。それならできそう

## step2

### 他の人のコード

> お、ちょっと私の期待とは違うアルゴリズムでした。
> これは関数型言語のデータ構造という背景がある問題に見えます。

https://discord.com/channels/1084280443945353267/1206101582861697046/1232739063891492895

これは面白い。
> 手続き型を使っている人は（関数型言語を学ぶことで）保守性を高めることができる

https://github.com/colorbox/leetcode/pull/15


https://github.com/naoto-iwase/leetcode/pull/67


https://github.com/huyfififi/coding-challenges/pull/13#discussion_r2082023838


https://github.com/ryosuketc/leetcode_grind75/pull/13#discussion_r2326285441

> Alternatively, a well-known implementation of a purely functional queue is to use two lists. One for enqueue and another for dequeue. Enqueue would simply cons with the enqueue list. Dequeue takes the head of the dequeue list. When the dequeue list is shorter than the enqueue list, refill it by reversing the enqueue list. See Chris Okasaki's Purely Functional Datastructures.

> A common representation for purely functional queues [Gri81, HM81, Bur82] is as a pair of lists, F and R, where F contains the front elements of the queue in the correct order and R contains the rear elements of the queue in reverse order.

> Elements are added to R and removed from F , so they must somehow migrate from one list to the other. This is accomplished by reversing R and installing the result as the new F whenever F would otherwise become empty, simultaneously setting the new R to [ ]. The goal is to maintain the invariant that F is empty only if R is also empty (i.e., the entire queue is empty).

> Banker's Method: 実際にはかかっていない計算量をかかったとみなして貯金し、必要に応じてそれを使う。

> 今回の問題の例では、

> push() -> 実際には操作は1回だが、2回としておく pop() -> 基本的には1回。frontのstackが空の時、rearのstackからmの要素を移してくるのだが、rearにm個要素がある -> 既にpush()がm回呼ばれている -> mの貯金があるので、それを使用して1回の操作とみなせる。

> そうすると、全てならして、1回の操作における時間計算量はO(1)になる。



レビュー：
> 個人的にはpythonで空のコレクションを定義するときはtype hintを入れるのが好みですが、この練習会でどこまで実務的に書くかは人によるかもですね！

これは使ってみようかな


書き直す。変数名はLLMと協力して作成。

_ensure_dequeue_readyは良い名前だな。

## 背景知識のまとめ

### 問題が言っていること

- **キュー（FIFO）**は「先に入れたものが先に出る」。**スタック（LIFO）**は「後に入れたものが先に出る」。どちらも「一端だけ」触れる制約が似ているので、**スタックを二つ**組み合わせてキューっぽい取り出し順を作れる。
- LeetCode の本文は操作ごとの計算量を聞くことが多いが、**Follow-up は「償却（amortized）O(1)」でよい**、というのがこの問題の現実的なゴールになっている。

### 標準解法（償却 O(1)）の構造

- **enqueue 用スタック**（入力側）と **dequeue 用スタック**（出力側）を持つ。
- **`push`**: 入力側にだけ `push`（移動なし・O(1)）。
- **`peek` / `pop`**: 出力側が空のときだけ、入力側をすべて出力側へ移す（入力の上から取って出力へ積む＝**一回の reverse 相当**）。出力側にデータがある間は、入力側へ**戻さない**。
- **不変条件の例**: 「出力側に要素があるとき、キューの先頭は出力側のトップ」「移動は出力側が空のときのみ」。これが書けると実装と名前が決まりやすい。


### 関数型データ構造との対応

- **純粋関数型のキュー**では、**前リスト F（front）と後ろリスト R（rear）**で表すのが定番。enqueue は **R 側へ寄せる**、dequeue は **F の先頭**。**F が尽きそう／尽きたら R を reverse して新しい F にする**（同時に R を空にする）、という「まとめて反転して補充」が、手続き型の **「出力スタックが空のときだけ入力スタックから全部移す」**と対応する。
- **Chris Okasaki**『Purely Functional Data Structures』やスライド資料が、この系統の背景としてよく引用される。引用メモにあるとおり、キューを **F と R のペア**と見なし、**F が空になるようなら R を反転して F にする**、という不変条件が教科書的。

### Banker's method

- 各要素は「入力スタックに載る」→「必要になった一度だけ、出力スタックへまとめて移る」→「pop で出る」と考えると、**スタック間の移動は高々 1 回（要素あたりの追加コストは定数）**になりやすい。
- **Banker's method（貯金）**のイメージ: `push` を実際より少し「高く」見積もって貯金し、`pop` 側で出力スタックが空のときの **まとめて m 個移す**コストを、その貯金で **均した 1 操作分**として説明する、という発想。

### 償却解析の一般論（[Wikipedia: Amortized analysis](https://en.wikipedia.org/wiki/Amortized_analysis)）

- **目的**: 単一操作の最悪コストだけを見ると高く見積もりすぎることがあるので、**操作の系列（データ構造が状態を持ち続けるとき）**について、コストを **系列全体でならす**考え方。
- **平均ケースとの違い**: 償却解析は **入力分布を仮定しない**議論として説明されることが多く、「確率的な平均」とは区別される（系列に対する分析というニュアンス）。
- **代表的な三手法**（いずれも同じ結論に行けるが使い分け）:
  - **Aggregate（総和）**: _n_ 回の操作の総コストの上界 _T(n)_ を取り、償却コストを **T(n)/n** とみなす。
  - **Accounting（会計／貯金）**: 操作ごとに償却コストを割り当て、早い段階で **実コストより多めに支払ってクレジットを蓄え**、後から重い操作に充当する（Banker's method）。
  - **Potential（ポテンシャル）**: データ構造の状態に **ポテンシャル関数**を置き、実コストにポテンシャルの増減を足したものを償却コストとする。
 O(n) でも、系列では **償却 O(1)** と説明できる例として載っている。


関数型言語はいつか勉強したい
