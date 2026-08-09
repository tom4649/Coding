# 57. Insert Interval

## step1
簡単そうに思ったが、添字などで混乱した。30mぐらいかかった

計算量 O(n)

## step2

### 他の人のコード

https://github.com/colorbox/leetcode/pull/2

> https://discord.com/channels/1084280443945353267/1206101582861697046/1215220860319965215

> 今感じていることは、「ゲームの最速クリア動画と攻略本を参考に、言われた操作をそのままやったらクリアーしました。」なんですよ。

> で、そうではなくて、こういう小さな道具をどれくらいの時間で書けるかを計画して見積もれる、その能力自体が大事です。

自分もまだAcceptedを気にする癖が抜けない

> 簡単なのを大量に書いて、安定感を出すのが大事だと思います。

> vector<vector<int>> で管理しているのが不便すぎます

二分探索で解く時はunpackした配列を作るのが分かりやすい


https://github.com/ryosuketc/leetcode_grind75/pull/26

> 先頭から intervals を見ていく。左にあるやつはそのまま出力。 オーバーラップしていたら、newInterval を更新。(破壊するのが嫌ならば別の変数にあらかじめコピーしておく。) オーバーラップしなくなったら newInterval を出力。 残りをすべて出力。
> これが私は一番素直だと思いました。

自分その解法が初めに浮かんだ

https://github.com/naoto-iwase/leetcode/pull/72

> in_placeかどうか引数で選べるようにした

なるほど

https://github.com/huyfififi/coding-challenges/pull/26

ソートしなおし、以前の問題で見たマージを適用する解法


挿入ときいてbisectも思いついたので書く

最悪計算量は O(n) だがこちらの方が速そう
