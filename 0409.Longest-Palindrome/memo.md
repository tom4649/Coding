# 409. Longest Palindrome

## step1
解くだけなら 5分ぐらい

## step2

Counterで書き直す、変数名の改善

> 正攻法でないものとして、Manacher's algorithm というのがあります。

別の問題の解法

https://leetcode.com/problems/longest-palindromic-substring/description/?envType=problem-list-v2&envId=rab78cw1

(忘れていたので書き直していても良いかもしれない)

https://github.com/Kitaken0107/GrindEasy/pull/27#discussion_r1656471861

https://github.com/huyfififi/coding-challenges/pull/17

https://github.com/NobukiFukui/Grind75-ProgrammingTraining/pull/31

https://github.com/ryosuketc/leetcode_grind75/pull/17

おおむね同じ解法だが 1 pathの書き方を真似しておく。 最後は `len(s) - odd_count + 1`としている。
