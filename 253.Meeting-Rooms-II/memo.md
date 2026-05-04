# Meeting Rooms II

https://neetcode.io/problems/meeting-schedule-ii/question

座標圧縮といもす法を使った解法: sol1.py
特に詰まるところはなかった
変数名などをリファクタリング: sol2.py
- 時間計算量 O(n log n): 時刻のソート O(n log n) + 配列構築 O(n) + 累積和 O(n)
- 空間計算量 O(n): sorted_times / time_to_rank / timeline それぞれ O(n)

start と endはペアである必要がないことに気が付いた: sol3.py
対応するendの前にstartがあるはずなので、endが出る前に現れたstartの数を覚えておけばよい
- 時間計算量 O(n log n): starts と ends のソート 2 回 + 線形走査 O(n)
- 空間計算量 O(n): starts / ends の格納に O(n) (Python の `sorted` は新しいリストを作るため。in-place ソートにすれば O(1))

### コメント集

https://github.com/nittoco/leetcode/pull/45#discussion_r1996402752

> これは意味づけの仕方次第じゃないですか。たとえば、ここの会社では、会議が始まるときに受付に鍵を借りに来て、終わるときに受付の郵便箱に返します。あなたは受付です。会議が始まるたびに、郵便箱の中の鍵を回収して、手持ちの鍵を渡します。会議室の予約の表が与えられるので、最低いくつ鍵が必要か答えてください。

heapを使う解法もあるのか

https://github.com/Ryotaro25/leetcode_first60/pull/61#discussion_r2005183830

> end, start がこの辞書順であることを利用していることに気がつけというのは、結構パズルを作っていると思います。

これは分からなかった。endが常にstartよりも前に来ないと成り立たないのか。

https://github.com/olsen-blue/Arai60/pull/57#discussion_r2027474114

> MAX_RANGE 使っていない解法をちょっと読み直してみませんか。

> 座標圧縮した結果の解法がいきなりでてきませんかね。

> まあ、これでもいいんですが、座標圧縮と同等のことが対応表を作らなくてもできますよね。たとえば、(start, +1), (end, -1) からなる集合を作ってソートするなど。

座標圧縮しか思いつかなかった

なるほど、しかし見方を帰ると自分の sol3.py も似たようなことをやっている

ペアの並び替えを使って書く: sol4.py
- 時間計算量 O(n log n): イベント生成 O(n) + 2n 個のタプルのソート O(n log n) + 線形走査 O(n)
- 空間計算量 O(n): time_and_change に 2n 個のタプル

https://github.com/olsen-blue/Arai60/pull/57#discussion_r2027474114
heapを使った解法: sol5.py
人の答えを見た後だからかけた。スッキリかけて感動。
- 時間計算量 O(n log n): 開始時刻でのソート O(n log n) + 各 interval に対する heap 操作 O(log n) を n 回 = O(n log n)
- 空間計算量 O(n): heap には最大で同時並行している区間数（最悪 n 個）の終了時刻が積まれる
