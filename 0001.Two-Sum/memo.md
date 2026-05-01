# 1. Two Sum

- [1. Two Sum](https://leetcode.com/problems/two-sum/description/)
- 愚直にsol1.pyを書いてしまった
- ハッシュを使うのが模範解答
    - https://discord.com/channels/1084280443945353267/1201211204547383386/1207251531041210408

### 解き直し
- sol3.pyをかけたがHashmapをつかうことが頭にあったおかげだと思う
- コメントなどを見直して修正: sol4.py

計算量の見積もり
sol1.py (愚直な解法): 時間 O(n^2), 空間 O(1)
sol2.py (Hashmap): 時間 O(n), 空間 O(n)

入力長の最大値が10^4である場合、Pythonでは
sol1.pyでは 10^4^2 / 10^7 = 10秒程度
sol2.pyでは 10^4 / 10^7 = 10^-3 秒程度
である

実際、LeetCodeでは
sol1.py: 1953 ms
sol2.py: 0ms
であったので大きく外れた見積もりではなさそう
