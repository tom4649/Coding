# 252.Meeting Rooms

https://neetcode.io/problems/meeting-schedule/question

始まる順番が早い順に並べて、、前の会議が終わるより早く始まるものがないかを調べる: sol1.py
時間計算量 O(nlog n)
破壊的に書いたが、非破壊的にするにはsortedを使えば良い

いもす法を使って解く: sol2.py
今回の問題では冗長だと思う
