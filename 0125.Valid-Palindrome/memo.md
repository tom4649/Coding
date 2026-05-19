# 125. Valid Palindrome

## step1
外側から判定していくO(len(s))解法。数字を無視しして一度間違えた。

## step2

### 他の人のコード

> 本質的にはそれほど変わりません。
>
> アルファベット以外を取り除く。
> 小文字にする。
> 頭からたどったものと尻からたどったものが同じかを確認する。
>
> これ、3つのループにもできますし、1つのループにもできます。

自分は1つのループで解いた。

https://github.com/hayashi-ay/leetcode/pull/9

isalnum()メソッドは知らなかった

https://docs.python.org/ja/3/library/stdtypes.html#str.isalnum

> A character c is alphanumeric if one of the following returns True: c.isalpha(), c.isdecimal(), c.isdigit(), or c.isnumeric()

ただし `isalpha() or isdecimal()`より範囲が広い

mapを使う書き方も参考になる

https://github.com/naoto-iwase/leetcode/pull/63

- `re.findall(r"[a-zA-Z0-9]", s)` で抽出 -> 小文字化 -> 両端比較。ASCII の英数字に限定したい意図なら正規表現がはっきりする。
- `isalnum()` は Unicode の「数字」まで拾う。問題の解釈次第。

https://github.com/TaisukeFujise/leetcode_tafujise/pull/10

https://github.com/Kitaken0107/GrindEasy/pull/8


