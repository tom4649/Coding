# 45. Jump Game II

## step1
Greedyを思いついた。12mほど。

今の位置からjumpできる場所の中で最も遠い場所にjumpすれば良い。O(nums.length)

dpを考えてみると O(nums.length * nums[i]) の解法になった。

## step2
dpの更新式の内側で参照される値は単調増加なので O(nums.length) にできる。solutionを見てから気づいた。


## step3
TODO: dpを書き直す
