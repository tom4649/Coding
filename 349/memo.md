# 349. Intersection of Two Arrays

- [リンク](https://leetcode.com/problems/intersection-of-two-arrays/description/)
- 愚直にsol1を書いた。悪くはないと思う。O(l1 + l2)
- https://github.com/mamo3gr/arai60/blob/main/349_intersection-of-two-arrays/memo.md
    - setの共通部分を取れば一行
    - set.intersection(iterable)のset側が短い方が良い
    - 「公式にはエラーの起こりにくさと読みやすさの観点から&よりintersectionが推奨されていますね」らしい
- 長い方(l1とする)がソート済みの場合、O(l2 logl1)
- マージソートぽい解答
    - 真似して書いてみる（sol3）
    - 実行時間は上とほぼ同じ。組み込みのソートは高速ということなんだろう
    - https://github.com/tarinaihitori/leetcode/pull/13#discussion_r1827026532
    - https://github.com/mamo3gr/arai60/blob/main/349_intersection-of-two-arrays/step2.py
