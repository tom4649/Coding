# 46. Permutations

https://leetcode.com/problems/permutations/description/

見たことあるやつだと思いながら自分では書けず、調べた
next permutationというアルゴリズムを学んだ
時間計算量 O(N N!)、空間計算量 O(1)
後からdeepcopyを使う必要はないことに気がついたので書き直す

- mutableなオブジェクトを含むオブジェクト：深いコピー
- immutableなオブジェクトだけを含むオブジェクト：浅いコピー


itertoolsにも実装がある: sol2.py

https://github.com/naoto-iwase/leetcode/blob/0046-permutations/0046-permutations/0046-permutations.md#%E5%AE%9F%E8%A3%852

https://github.com/mamo3gr/arai60/blob/46_permutations/46_permutations/memo.md

https://leetcode.com/problems/permutations/solutions/18239/a-general-approach-to-backtracking-questions-in-java-subsets-permutations-combination-sum-palindrome-partioning/

バックトラック：「探索中に一時的に状態を変更し、再帰から戻るときに必ず元に戻す DFS」

おそらくこの問題の題意はこれだろう。
スタックと再帰関数で実装する

sol3.py
人のコードを一通り見た後に空で書くとこうなった
時間：O(n n!)、空間：ざっくりO(n n!)
- geminiにrevisedさせるとビットマスクを提案された

sol4.py
geminiにrevisedさせると順序一定のためにsortを提案された
値に重複があるときはindexで持つべきだろう




