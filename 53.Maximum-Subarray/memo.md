# 53. Maximum Subarray

- 愚直にsol1.pyを書いた
    - 計算量 O(n)
- Kadaneのアルゴリズム
    - https://en.wikipedia.org/wiki/Maximum_subarray_problem
    - https://qiita.com/awesam/items/37a0ceb1468feef3a403
    - https://ark4rk.hatenablog.com/entry/2018/01/08/002508
    -  自然言語で説明すれば、「arrayを一巡し、各要素(a_iとする)で終わるものが最大値になりうるかを検証する。一つ前の要素で終わったsubarrayの最大値を記録しておけば、それにa_iを加えたものかa_iだけのsubarrayがa_iで終わったarrayの最大値である」
    - sol2.py
- https://discord.com/channels/1084280443945353267/1206101582861697046/1207518775851876362
    - sol1.pyと同じ考え
- https://github.com/mamo3gr/arai60/blob/53_maximum-subarray/53_maximum-subarray/step1.py
    - cumulative sumって配列の最初からではなくてもそう呼ぶのかな
- https://github.com/mamo3gr/arai60/blob/53_maximum-subarray/53_maximum-subarray/step3.py
    - > マイナスなら相続をやめる
- https://github.com/mamo3gr/arai60/blob/53_maximum-subarray/53_maximum-subarray/step2.py
    - 分割統治法, O(Nlog N)



### 解き直し
sol1.pyと同じ解法が最初に思いついた
