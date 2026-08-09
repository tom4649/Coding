# 90. Subsets II

## step1
Arai 60の問題を覚えていたので、その応用で解けた。12mほど。

時間、空間 O(n)

Arai60の問題: https://leetcode.com/problems/subsets/

もう少し簡潔にもできる

~~ バックトラック ~~ 再帰 でも解く

subsets[:] とすれば extention という変数を用意しなくてもかける

## 他の人のコード
https://leetcode.com/problems/subsets-ii/solutions/6877292/video-sorting-the-input-array-to-remove-wzqim/

バックトラックはこの方法だ

再帰をバックトラックで書いたつもりになっていた

## step2
バックトラック
subsets.append(subset)として間違えた

## step3
バックトラック
