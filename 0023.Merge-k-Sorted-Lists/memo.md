# 23. Merge k Sorted Lists

## step1

17mで解けた。紙に書いて考えるうちに最小値を管理する -> heapという発想になった。破壊的な解法になっている。

時間計算量：
O(sum(lists[i].length)log k)

空間計算量：
O(k)

## step2

非破壊的な解法: step2.py

indexを格納しないと、<が定義されずエラーになる。

これを面接のtest環境のないところで気がつくのは、ヒントがないと自分には難しそう。

以下の実験でも確認できる。

```python
heap = [(0, ListNode()), (0, ListNode())]
heapq.heapify(heap)
# TypeError: '<' not supported between instances of 'ListNode' and 'ListNode'
```

## 他の人のコード

https://github.com/shining-ai/leetcode/pull/67

> これ (index) がないと、定義されていないListNodeの比較になって問題が出るのですかね。

- 非破壊的+heapを使わない解法：

```python
lass Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lists_val = []
        for node in lists:
            while node:
                lists_val.append(node.val)
                node = node.next
        lists_val.sort()
        sentinel = ListNode()
        node = sentinel
        for i in lists_val:
            node.next = ListNode(i)
            node = node.next

        return sentinel.next
```

LinkedListの操作に気を取られて思いつかなかった。

時間計算量的はS=sum(lists[i].length)として O(Slog S)だが実際に実行してみると、heapの解法と大差なかった。


> マージソートをイメージした解法
> 先頭の2つのリストをマージしていき、最後の1つになるまで繰り返す

自然な解法なので、面接で聞かれる可能性は高そう。これを思いつかなったのは、まだまだ修行が足りないということだろうな。

時間計算量 O(Slog k)

sentinelという変数名は良いな

```python

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge_two_lists(list_1, list_2):
            sentinel = ListNode()
            node = sentinel
            while list_1 and list_2:
                if list_1.val < list_2.val:
                    node.next = list_1
                    list_1 = list_1.next
                else:
                    node.next = list_2
                    list_2 = list_2.next
                node = node.next
            if not list_1:
                node.next = list_2
            else:
                node.next = list_1
            return sentinel.next

        list_queue = deque(lists)
        if not list_queue:
            return None
        while 1:
            list_1 = list_queue.popleft()
            if not list_queue:
                return list_1
            list_2 = list_queue.popleft()
            mearged_list = merge_two_lists(list_1, list_2)
            list_queue.append(mearged_list)
```

## step3
マージソートの解法を3回書くことにする。

merge_two_listsの内側でswapを用いることでsimpleになった気がする。
