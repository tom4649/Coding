# 347. Top K Frequent Elements
- [リンク](https://leetcode.com/problems/top-k-frequent-elements/description/)
- dict の初期化をして数え、その後 list にして sorted に key function を渡して k 個取る: これを見てsol2を書いた
    - https://discord.com/channels/1084280443945353267/1235829049511903273/1245555256360697949
- heapを使うと nlog kになる
    - https://github.com/sakupan102/arai60-practice/commit/3aaa67b3e359787797fcdad70255718480678643
    - heapq.heappop, heapq.heaptify
    - sol3
- クイックセレクトでもできる
    - sol4
    - 平均計算量 O(n)


### 解き直し
n: len(nums)
m: uniqueな値の個数
とすると平均時間計算量は
sol5, sol6: 平均, 最悪 O(n + m log m)
sol7: 平均, 最悪 O(n+mlog k)
sol8: 平均, 最悪 O(n+klog m)
sol9: 平均 O(n+m) 最悪 O(n+m^2)




### コメント集
https://discord.com/channels/1084280443945353267/1235829049511903273/1245555256360697949

> Counter を使うと、さすがに Counter の内部実装を書いて欲しいといわれるもの

> これ、実行順序が、items, sorted, slice, map, list ですよね。目が左右に動きます

