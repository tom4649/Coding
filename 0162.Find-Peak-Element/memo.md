# 162. Find Peak Element

## step1
16mほどかかった。閉区間の二分探索。閉開区間で書くとindexのアクセスが範囲外となりうるため。
閉開区間でも書いておく。

制約が小さいのでbrute forceを使っても実行時間は変わらない。

答えが複数あるときに返る値は未確定。しかし、例えば小さい index を返すように制約を加えると二分探索では解けなくなるように思う。
mid, left, right の情報を見て区間の山を特定することができないため。

単調性がないので bisect の使用は不適切なはずだが、と動く。同じ二分探索のロジックで書かれているため。

https://github.com/python/cpython/blob/main/Lib/bisect.py

## step2

LeetCodeの解法を眺めたが新しいものはない。
