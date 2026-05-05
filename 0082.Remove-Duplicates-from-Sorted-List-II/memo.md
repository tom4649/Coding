# 82. Remove Duplicates from Sorted List II
- [リンク](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/)

- sol1は煩雑でわかりづらい。何度か提出を繰り返して通した
- sol2は他の人のコードを読んでから見ないで書いた
- 可読性はsol2の方が高いが、sol1の方が実行時間は短い。ポインタの更新ではなく、ポインタの移動で値を書き換えているため

### 解き直し
すらすらと書けたが、変数名によくないと指摘されていたcurrentを使ってしまった
以前のコードを見て、混乱したコードを書いていた、と認識できるようになった
変数名を改善し、コメント集を読み直した
tail:「今どこまで処理済みなのか」
node:「次にどこを見ればいいのか」
dummyを用いた番兵も自然に解釈できる
