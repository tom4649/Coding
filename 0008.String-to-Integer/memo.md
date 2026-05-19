# 8. String to Integer (atoi)

- 言われた処理を愚直に行った: sol1.py

他の解法を思いつかない


### コメント集
https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0

> 一応、MIN = - MAX - 1 は念頭にありますね

これを考慮して一つの処理にまとめている

https://github.com/Yoshiki-Iwasa/Arai60/pull/64/changes/BASE..857ed449085ebae4c21cd475d45b541d6d43ccac#diff-dbf5e75b50aa4257946026d6539860be248a58856e1b457b4d37445059b05857


> Java には、multiplyExact、addExact というのがありますね。

Overflowを例外処理で扱う演算

https://github.com/Ryotaro25/leetcode_first60/pull/64/changes/BASE..37228575e7396054b8e8c0a649cfa8ba17881f05#diff-4d65a16d7dcb4ddd736f444c1721b5dc53e97518dd7101cfbcc4a81453dab075


C++のコンパイラに関する記述

久しくこうした話題に触れていなかった

https://github.com/mamo3gr/arai60/blob/8_string-to-integer-atoi/8_string-to-integer-atoi/memo.md

> intは符号もパースしてくれる

https://docs.python.org/3/library/functions.html#int

なるほど、これは知らなかった

https://github.com/naoto-iwase/leetcode/pull/60/changes

数値判定の組み込み関数

str.isdecimal: Unicodeの一般カテゴリ「Nd（Number, Decimal Digit）」に分類される文字を全てTrueにする

```python
>>> '１'.isdecimal()
True
>>> '一'.isdecimal()
False
```

str.isdigit()
文字列中の全ての文字が数字で、かつ 1 文字以上あるなら True を、そうでなければ False を返します。ここでの数字とは、十進数字に加えて、互換上付き数字のような特殊操作を必要とする数字を含みます。また 10 を基数とした表現ができないカローシュティー数字のような体系の文字も含みます。正式には、数字とは、プロパティ値 Numeric_Type=Digit または Numeric_Type=Decimal を持つ文字です。


str.isnumeric()
通常の数字に加えて、Unicodeの数値属性（numeric value property）を持つすべての文字が含まれます。例えば U+2155（1/5を表す分数文字：⅕）などがこれに該当します。厳密な定義では、Unicodeの属性が Numeric_Type=Digit、Numeric_Type=Decimal、または Numeric_Type=Numeric のいずれかである文字を指します。

上から下に範囲が広がっている

正規表現を用いた実装も参考になった。自分でも書いてみる: sol2.py

https://docs.python.org/ja/3/library/re.html



Pythonを使っていたので意識していなかったが、32bit制約のOverflowを防ぐことを意識して書く: sol3.py
