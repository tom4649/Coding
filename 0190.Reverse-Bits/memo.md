# 190. Reverse Bits

## step1
strに直してreverseする。f-stringのフォーマットが分からず、調べた。

https://docs.python.org/ja/3/tutorial/inputoutput.html#formatted-string-literals
https://docs.python.org/ja/3/library/string.html#formatspec

bが2進数、x (Xで大文字)で16進数、#を付けるとプレフィックスが付く

0(桁数)で0埋め。他を書くときには><^などを書く

```python
>>> num = 42
>>> print(f"{num:b}")
101010
>>> print(f"{num:x}")
2a
>>> print(f"{num:#x}")
0x2a
>>> print(f"{num:#X}")
0X2A
>>> print(f"{num:03b}")
101010
>>> print(f"{num:03x}")
02a
>>> print(f"{num:-3x}")
 2a
>>> print(f"{num:,3x}")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: Invalid format specifier ',3x' for object of type 'int'
>>> print(f"{num:,>3x}")
,2a
>>> print(f"{num:,^6x}")
,,2a,,
```

bit演算でも書く。

## step2
https://github.com/Kitaken0107/GrindEasy/pull/23

> 文字列に変換しないでやってみてください。ビット操作の問題だと思います。

> 32 bit 整数って、シフト演算をして、最下位ビットを見ると、スタックみたいなものじゃないですか。
