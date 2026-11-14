# 622. Design Circular Queue

## step1
doubly linked list で実装した。が、この実装だと Circular のメリットがない。

## step2
配列の長さが決まっているならメモリの動的確保が必要なくなる

今回、削除時に上書きを行っていないが、オブジェクトが巨大な場合は削除時にNoneで上書きすると、GCでメモリを節約できる。
