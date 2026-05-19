# 39. Combination Sum

https://leetcode.com/problems/combination-sum/description/

nonuniqueな解を全て列挙してtupleにしてからuniqueにする回答方針: sol1.py

入れる順番を前からに固定すれば uniqueになる: sol2.py

DFSでも解ける: sol3.py
このバックトラック続きの問題の中になかったら思いついていないと思う

関数にしつつバックトラックがわかりやすいようにした: sol4.py

計算量がわからない
時間計算量: O((target/min(candidates))^{n})
空間計算量: O(target/min(candidates))


### コメント集

> https://discord.com/channels/1084280443945353267/1235829049511903273/1265717341178822787

https://github.com/fhiyo/leetcode/pull/52/changes

yieldを用いた解法

https://discord.com/channels/1084280443945353267/1233295449985650688/1242118169968115845
計算量の見積もり

https://discord.com/channels/1084280443945353267/1233295449985650688/1242103186009886862
分割数
https://github.com/Mike0121/LeetCode/pull/1#discussion_r1578212926

> 答えの数ですが、candidates = [1..target] の場合、これは分割数というものですね。

> 分割数の極限は、ハーディとラマヌジャンが求めています。
> a(n) ~ 1/(4nsqrt(3)) * e^(Pi * sqrt(2n/3)) as n -> infinity (Hardy and Ramanujan)
> https://oeis.org/A000041
> だいたい、13^sqrt(n) / 7n くらいですか。

### 解き直し
sol7_retry.pyを解く時にやや混乱した
exclude: index+1
include: index
を渡す
