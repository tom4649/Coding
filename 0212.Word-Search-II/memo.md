# 212. Word Search II

## step1

通常の DFS でTLE

Trie 木を使ったが TLE

## step2

AIにTrie Node 渡すコードを書いてもらい、ほぼ写経。

毎回 startwithで検索していたところが overhead だった。
borad を一時的に書き換えて訪問済みを管理する。

計算量：

文字列の長さを L とする

文字の数を W とする

DFS:

時間：O(WMN3^{L})

空間：O(L)

Trie Node:

時間：O(WL + MN3^{L})

空間：O(WL)
