# Nested Transactional Key-Value Store

## step1

https://www.screna.ai/experience/353878d2-8c78-44ec-b945-fda1a752cf3f

を参考に解いた

value が immutable なとき、dict のdeepcopy は不要だった

値を変更するとき、valueはimmutableなので、新しくobjectが作られる

## step2
AIに begin が O(1) になるコードを書いてもらった。

