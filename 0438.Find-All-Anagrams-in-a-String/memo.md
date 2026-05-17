# 438. Find All Anagrams in a String

## step1

ナイーブな判定機を作り、次にanagramが出現しうる場所までスキップする方針。

25mぐらいかかった。方針を思いつくのよりも変数の取り間違え、添字のミスで時間を消費。添字にはもっと慣れる必要がある。

O(len(s)len(p))。遅い方だったので改善できるのかもしれない

## step2

https://github.com/huyfififi/coding-challenges/pull/62

Sliding Windowを使うと O(len(s))となる。この解法の方が自然にも思える。

- 当初 `ord` を「文字コード依存」のように感じ `string.ascii_lowercase.find` を採用。冗長さは認識していた。
- `dict` / `Counter`は、将来ほかの文字種に広げる要件が出てからでよいとしスキップ。カウント 0 のキーを払う手間で少し複雑になるイメージだったとのこと。
- `ord` は Unicode のコードポイントを返しエンコーディングとは無関係。
- `find` は文字列を毎回線形探索

標準ライブラリstring知らなかった。string.ascii_lowercase.findを呼ぶと毎回26ステップかかることになる。

https://docs.python.org/ja/3.13/library/string.html

> ordはUnicodeのコードポイントを返すので、エンコーディングは関係なく、いつも同じ値を返します。findの線形探索のコストが気になりました。

なるほど


> そこまで時間をかけずに方針を立てることができたが、ループの end 範囲を間違えて (`len(source) - anagram_length + 1` を `len(source) - anagram_length` としてしまった)、延々とハマっていた。何度見直しても、変な思い込みで間違っている部分をスルーしてしまうから、インデックスの境界に気をつけなければならない問題は苦手だな。

自分も同じところで間違えた。

整理すると

(last =) start + len(p) − 1 < len(s) <-> start < len(s) − len(p) +

は同値。似たケースで間違えないようにしたい。
