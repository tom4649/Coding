# 373. Find K Pairs with Smallest Sums

- [リンク](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/)
- ヒープを使って書いたが時間がかかった
- これは勉強になる。マージソートのようなアルゴリズム。yieldが遅延評価なのでメモリ消費量も少ない。また、j_middleまではsumを比較する必要がない
    - https://discord.com/channels/1084280443945353267/1235829049511903273/1246303084435607682
    - sol2は写経

### 解き直し
sol3.pyを書いたがheapを使う考え方と解いたときの記憶が残っていたので書けたような気がする
