# 552. Student Attendance Record II

## step1
DP で解くことを思いつく。next_contain_aの更新式の誤りに気づかず時間を消費。22m程度。

変数名を改善。

## step2

dp を使う解法には配列をつかうものもある

https://leetcode.com/problems/student-attendance-record-ii/solutions/415467/python-olog-n-using-numpy-by-lxnn-fy96/?envType=problem-list-v2&envId=7p55wqm

行列累乗。フィボナッチ数列と同じ考え方。計算量がO(log n)になる。

## step3
行列累乗を書く
