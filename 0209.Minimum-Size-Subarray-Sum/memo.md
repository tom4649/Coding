# 209. Minimum Size Subarray Sum

-　sol1.py: 何も見ないで書いた。sliding windowで解ける。O(n)。

https://github.com/SuperHotDogCat/coding-interview/pull/31/changes

二重のwhile文で書いている。rightの始まりと終わりは確定しているので、個人的にはfor文が良いのではないかと思った。
min_length = len(nums) + 1とするのはなるほど。ただ分かりやすさではinfでも悪くはないと思う。

https://github.com/olsen-blue/Arai60/pull/50/changes/BASE..1b460a0c97f2ef17efe579db6835cb0623d6cf67#diff-6d4eb2707ed57d8037bfa2e5985424b237a407741a7602ba92b31e090d1cb096

https://github.com/naoto-iwase/leetcode/pull/50

二分探索と分割統治法で書く。計算量はO(nlogn)になる
二分探索 -> 自分で書くと、leftのindexの処理が彼と異なった。leftを含めるか否か。

二分探索の方は自分でも思いついただろう（今回は人の答えを見たが）
分割統治法は人のを見て初めて気づいたので、頭に入れておきたい



