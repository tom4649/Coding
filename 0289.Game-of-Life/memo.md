# 289. Game of Life

## step1
愚直に解いたが、空間計算量が O(rc) となる

## step2
constantにしたい。AIにbitで管理する方法を教わった。

---

> Follow-up 1: Gridがメモリに収まらない場合

Row-by-Row Processing:

1. 入力ファイルから3行を読み込む。
2. 中央の行の次の状態を計算する。
3. 結果を別のファイルに書き込む。
4. 1行ずつスライドして繰り返す。

> Follow-up 2: liveが少ない場合

-> step2_sparse.py

set を使って生きている cell だけを管理

何世代も繰り返す場合にはこのように書くのがよさそう。

