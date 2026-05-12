# 981. Time Based Key-Value Store

## step1
二分探索を使えば制約は守れそう

10mぐらい

bisect_leftとbisect_rightで迷った

index = bisect_left() -> timestamps[index] >= timestamp, timestamps[index - 1] < timestam

index = bisect_right() -> timestamps[index] > timestamp, timestamps[index-1] <= timestamp

## step2

場合分けは簡潔にできる

https://github.com/huyfififi/coding-challenges/pull/47/changes#diff-54fa07dd0f31f16402c4d471600cc6b8bfa7a9ed860a628aeb48c49d257adb28

pairの配列として持つこともできる。defaultdictを使うと便利


## step3

bisectを使わずに書く

一発でかけた
