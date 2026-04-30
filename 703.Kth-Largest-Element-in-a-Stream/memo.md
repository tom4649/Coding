# 703. Kth Largest Element in a Stream
- heapq https://docs.python.org/3/library/heapq.html を使った（知らなかったのでググった）
- 降順にもできる: heapq.heapify_max(x)
- sol1のロジックをsol2でやや整理
- ヒープ：構築 O(n), 最小値取り出し O(log n)
- 今回の add の計算量は O(log k)
- https://discord.com/channels/1084280443945353267/1183683738635346001/1185260183648215090

### Quicksort - Wikipedia
- 分割統治法、最悪O(n**2)、平均O(nlog n)
- pivot 選択：random, 中央値
- 末尾再帰最適化：
    - Quick Sortで左側→右側と配列をsortする場合、右側は関数の最後に呼ばれるため末尾再帰になっている。そのため右側の再帰呼び出しはループに変換できる（小さい側を再帰するらしい）



### Merge Sort
- 呼び出した後に配列を合わせるので、常に分割が半分、最悪 O(nlog n)
- キャッシュを考えるとクイックソートの方が早い場合が多い
- Merge sortは
    - 補助メモリが必要
    - 離れた場所の二つの配列要素を比較する
    ため

### Quick Select
- 平均：O(n) 片側しか探索しないため
- 最悪：O(n**2)

