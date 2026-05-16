# 5. Longest Palindromic Substring


最悪O(n^3)ならすぐ思いつく: sol1.py
計算時間 10^9 / 10^7 = 10^2

中心から展開すれば O(n^2): sol2.py

### コメント集

Manacher's algorithm: 知らなくて良い

https://en.wikipedia.org/wiki/Longest_palindromic_substring#Runtime

https://github.com/usatie/leetcode/blob/main/Blind75/03.%20Longest%20Palindromic%20Substring/ans_03_20240129_Manacher's%20Algorithm_refactored.cpp

https://snuke.hatenablog.com/entry/2014/12/02/235837

1. 奇数長の回文候補に変換する
2. すでに分かっている対称位置の半径を借りる
3. 足りない外側だけ追加で確認する
4. より右まで届いたら center/right を更新する

> 関数の切り出しの方法として、そもそも何に興味があるのかを考えましょう。
> 今回の場合だと、読んでいる人は、palindromeRadii の構築に興味があるはずなので、何でそれが決まっているのかが大事で、それは残して、後は切り出せばいいように思います。
> そうすると、「基本的には、頭から真面目に調べていくのだが、過去の情報から計算できるときがあるのでそれを使い、過去の情報から中途半端に分からないときもあるのでそのときはそこから再開」という部分を残して後は切り出すという話なのかと思います。

読む人が知りたいのは「Manacher がどうやって radius[idx] を構築しているか」なので、メインループにはその構造だけを残す。細かい左右比較や半径計算の詳細は関数に逃がすと読みやすい。

計算量は O(n^2)ぽく見えるがO(n)


### 他の人

https://github.com/huyfififi/coding-challenges/pull/56/changes#diff-88e4497fd99389071837affe590f79f66bd55501f7ad90eaa3a414101c7046b5
二次元DPでも解ける。なるほど
各判定O(1)なので合計計算量は O(n^2)
