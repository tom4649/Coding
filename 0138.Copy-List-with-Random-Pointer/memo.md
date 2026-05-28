# 138. Copy List with Random Pointer

## step1

頭から実装するとstep1.pyとなった。

同じ処理が現れたので関数化したが、getattrなどが何度も現れてわかりづらい

## step2

ソリューションを漁る

https://leetcode.com/problems/copy-list-with-random-pointer/solutions/379056/python-solution-with-comments-on-using-a-xf3k/?envType=problem-list-v2&envId=7p5x763

再帰を使うのは思いつかなかった
```python
def copyRandomList(self, head: 'Optional[Node]', seen={None: None}) -> 'Optional[Node]':
    """ O(N)TS """
    if head not in seen:
        seen[head] = Node(head.val)
        seen[head].next = self.copyRandomList(head.next, seen)
        seen[head].random = self.copyRandomList(head.random, seen)
    return seen[head]
```

https://leetcode.com/problems/copy-list-with-random-pointer/solutions/7052593/on-and-o1-solutions-by-russelldcosta-lbh8/?envType=problem-list-v2&envId=7p5x763

Hashmapを使わずに解ける。空間計算量がO(1)になる。
