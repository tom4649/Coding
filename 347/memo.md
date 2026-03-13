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


