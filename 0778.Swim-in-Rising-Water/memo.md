# 778. Swim in Rising Water

## step1
自力で二分探索を思いつくことができた。計算量 O(n^2 logn)。

時間 t と grid の値の不等号の向きを間違えて時間を溶かした。21m。

## step2

> Use either Dijkstra's, or binary search for the best time T for which you can reach the end if you only step on squares at most T.

Dijkstraを使うのか。和ではなくmaxをcostの計算に使えばよい。こちらも計算量O(n^2 logn)。

BFSを毎回行う二分探索よりも定数倍速い。

---
https://leetcode.com/problems/swim-in-rising-water/solutions/7252184/swim-in-rising-water-3-approach-editoria-8zp6/?envType=problem-list-v2&envId=7p55wqm

Union-Find + Kruskal

## step3
TODO: Kruskal法を書く
