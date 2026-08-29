# 1937. Maximum Number of Points with Cost

## step1

dp を使えそうだと思った。計算量 O(mn^2) の解法しか思いつかず、TLE した解法: step1_TLE.py

28mほど経過して諦めて答えを見る

# step2

https://leetcode.com/problems/maximum-number-of-points-with-cost/solutions/1344888/c-dp-from-om-n-n-to-om-n-by-npes87184-waex/?envType=problem-list-v2&envId=7p55wqm

各行の更新にもDPをつかう。これで正しいのか分からなかったので考えてみる

 left[c]
= max_{i<=c}(dp_prev[i]  - (c-i))
= max_{i<=c}(dp_prev[i]  + i) - c
= max(max_{i<=c-1}(dp_prev[i]  + i), dp_prev[c] + c) - c
= max(max_{i<=c-1}(dp_prev[i]  + i) - (c - 1) - 1, dp_prev[c])
= max(left[c-1] - 1, dp_prev[c])

1マスずれるたびに一律に1ペナルティが発生するから前の列の値を使える

rightも同様

---

running_max という変数を使って配列の生成コストをなくす

これ以外の解法は思いつかない

## step3



