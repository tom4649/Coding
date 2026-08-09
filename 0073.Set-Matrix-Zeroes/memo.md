# 73. Set Matrix Zeroes

## step1
空間計算量O(n + m), 時間計算量O(mn)の解法。

> A simple improvement uses O(m + n) space, but still not the best solution.
> Could you devise a constant space solution?

わからない

## 他の人のコード

https://leetcode.com/problems/set-matrix-zeroes/solutions/6121398/video-o1-space-use-the-first-row-and-col-1kr7/

空間O(1)解法

https://github.com/thonda28/leetcode/pull/9

> 意味のある変数名にしたいです。num_rowsとかでしょうか？

問題文にあわせて m, nにしたがこちらの方がわかりやすいかもしれない

> 0行目と0列目のフラグをそれぞれ用意しなくても、matrix[0][0]をどちらかとみなせますね

読みにくくなると思うので二つフラグを持たせる方針でもよいのでは、と個人的には思う
