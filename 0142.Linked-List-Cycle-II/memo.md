# 142. Linked List Cycle II
- [LeetCode: Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)

- Floydの循環検出法
- ネタを知っていたが、コードを書けずにググりました
- 1回目で出会うところがちょうどサイクルの倍数になっているところがミソ

2回目: Floydの循環検出法をかけた。紙とペンで書かないと分からなかったが。

## C++

フォーマットの注意：if, while の () の前後に空白を入れる。ポインタの宣言の * の位置

スタイルガイド：https://google.github.io/styleguide/cppguide.html

https://github.com/hiratasec/leetcode/pull/4

https://github.com/liruly/leetcode/pull/3

https://github.com/liruly/leetcode/pull/1/changes/BASE..8c91bb1b095ed4df1f5e705ffb0d005f7f618ee7#diff-10326c16791f72537f09fca512633d1efa991fd916c76ab7d8e3e4e74f82e58d

> C++20 以降では std::unordered_set::contains() を使われることをおすすめします。

> 私は宣言と同時に初期化します。別にするのも古い C の流儀ですね。


