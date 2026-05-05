# 252.Meeting Rooms

https://neetcode.io/problems/meeting-schedule/question

始まる順番が早い順に並べて、、前の会議が終わるより早く始まるものがないかを調べる: sol1.py
時間計算量 O(nlog n)
破壊的に書いたが、非破壊的にするにはsortedを使えば良い

いもす法を使って解く: sol2.py
今回の問題では冗長だと思う

### 他の人のコード
https://github.com/mamo3gr/arai60/blob/253_meeting-rooms/253_meeting-rooms/memo.md

itertools.pairwise を使っている

自分でEvent Objectを作ってheapで管理する

イベントを時刻順・座標順に並べて、左から右へ走査しながら状態を更新する考え方をsweep lineと呼ぶらしい
