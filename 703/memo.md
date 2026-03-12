# 703. Kth Largest Element in a Stream
- heapq https://docs.python.org/3/library/heapq.html を使った（知らなかったのでググった）
- 降順にもできる: heapq.heapify_max(x)
- sol1のロジックをsol2でやや整理
- ヒープ: 構築 O(n), 最小値取り出し O(log n)
- 今回の add の計算量は O(log k)
