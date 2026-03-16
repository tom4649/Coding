# 108. Convert Sorted Array to Binary Search Tree
[リンク](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/)

- sol1.py: 1分ぐらいで書けて一発で通った
    - 再帰が一番素直な気がする

- https://github.com/colorbox/leetcode/blob/6df017863f41c02430b656fa3333d3cbbfe48d18/108/step2_3.cpp
    - ダブルポインターによる解法。
    - ポインタで保存先を表す
    - C, C++のポインタ忘れてるので機会があれば復習したい
- https://github.com/irohafternoon/LeetCode/pull/27/changes/BASE..6d5bfca367a0487c71117a848d66ffd4c6036136#diff-e8db98cc7e692ba9b347d75443f848723329eaf93d3002524ccc4f57d995dbee
    - メモリリーク

- https://github.com/mamo3gr/arai60/blob/108_convert-sorted_array-to-binary-search-tree/108_convert-sorted_array-to-binary-search-tree/memo.md
    - que, stackを使った実装がある
    - 選択肢として持てるようにしておきたい
