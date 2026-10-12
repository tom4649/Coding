# 792. Number of Matching Subsequences

## step1
hashtableと二分探索を利用して解いた。18mほど。

計算量: O(s.length + words.length * words[i].length * log (s.length))

変数名や書き方を改善。

## step2

バケットを使った解法：
https://leetcode.com/problems/number-of-matching-subsequences/solutions/1290406/cjavapython-process-by-bucket-picture-ex-xeoa/?envType=problem-list-v2&envId=7p55wqm

イテレータを使って書き直す。

計算量: O(s.length + words.length * words[i].length)

## step3
TODO
