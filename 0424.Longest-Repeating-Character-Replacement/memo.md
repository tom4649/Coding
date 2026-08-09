# 424. Longest Repeating Character Replacement

## step1
sliding windowを使う。
23mほどかかった。

時間計算量はO(N)。ただし文字列に含まれるユニークな文字を定数とみなした場合。

他の解法は思いつかない。Hashmapがヒントにあるがこれをどう使うのかわからない。

## 他の人のコード

https://github.com/olsen-blue/Arai60/pull/49#issuecomment-3649179920

https://github.com/Exzrgs/LeetCode/pull/48

hashmapの使い方はこうするのか

https://github.com/potrue/leetcode/pull/65/changes

maxを取り出す部分でheapを使った解法。

heapの遅延評価: heapからの削除が難しいからとりあえずcounterだけ更新しておいて、heapから取り出したときの値は一致していなかったら捨てる

実際にはheapの定数倍の計算量で遅くなるようだ。

https://leetcode.com/problems/longest-repeating-character-replacement/solutions/8301734/optimal-solution-by-nthapa000-lejz/

max_frequencyは更新されるときだけ計算しても良く、時間計算量が小さくなる。が、毎回計算した方がわかりやすいようにも思う。

## step2
