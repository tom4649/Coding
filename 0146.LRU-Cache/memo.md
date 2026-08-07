# 146. LRU Cache

## step1

DoublyLinkedListで解いた。これで書けるという事前知識があった。

バグをとって20mぐらいかかった

## step2
### 他の人のコード
https://github.com/t0hsumi/leetcode/pull/16
https://github.com/fhiyo/leetcode/pull/9/changes/19861c4d06a3212b97888a49e1b321e69031f63b

番兵は一つで良い。自分のstep1は一つ多かった。


https://github.com/Mike0121/LeetCode/pull/49

OrderedDictを使うと簡単に書ける。内部はDoublyLinkedList。

命名規則

https://peps.python.org/pep-0008/#descriptive-naming-styles

> - _single_leading_underscore: weak “internal use” indicator. E.g. from M import * does not import objects whose names start with an underscore.

> - single_trailing_underscore_: used by convention to avoid conflicts with Python keyword, e.g. :
tkinter.Toplevel(master, class_='ClassName')

> - __double_leading_underscore: when naming a class attribute, invokes name mangling (inside class FooBar, __boo becomes _FooBar__boo; see below).

> - __double_leading_and_trailing_underscore__: “magic” objects or attributes that live in user-controlled namespaces. E.g. __init__, __import__ or __file__. Never invent such names; only use them as documented.



__double_leading_underscoreを知らなかった
