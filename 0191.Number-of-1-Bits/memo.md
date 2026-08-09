# 191. Number of 1 Bits

## step1
1mもかからなかった。strでも書く。

## 他の人のコード
https://github.com/Ryotaro25/leetcode_first60/pull/76

> 整数の割り算は遅い、ビット演算は速い、という感覚は持っておいたほうが良いと思います
pythonだと差はなさそう

> 分割統治法による解法もあります。

この解法はおもしろい。有名な解法らしい。

足している数字はそれぞれ二進数で0101..., 00110011...,00001111...となっている。

一行目で2bitずつ区切った場所のbitカウントを2bitずつ2進数で表現し、二行目で4bit,..最終的に32bitのbitカウントになる。

> https://en.wikipedia.org/wiki/Hamming_weight#Efficient_implementation

1. 上の解法はtree patternと呼ばれている。
> For processors lacking those features, the best solutions known are based on adding counts in a tree pattern
> The above implementations have the best worst-case behavior of any known algorithm

2. 上の亜種がある。0x01010101をかける。筆算を考えるとわかりやすい。

以下でもいけるのではと思ったが、よく考えるとうまくいかない。4bitで、最大値を表現できないため

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        n = n & 0xffffffff
        n = (n & 0x55555555) + ((n >> 1) & 0x55555555)
        n = (n & 0x33333333) + ((n >> 2) & 0x33333333)
        return ((n * 0x11111111) & 0xffffffff) >> 28
```

3. &を取ると右端の1が消える。これも実装してみる。
> As Wegner described in 1960,[14] the bitwise AND of x with x − 1 differs from x only in zeroing out the least significant nonzero bit: subtracting 1 changes the rightmost string of 0s to 1s, and changes the rightmost 1 to a 0. If x originally had n bits that were 1, then after only n iterations of this operation, x will be reduced to zero. The following implementation is based on this principle.

4. 大きなメモリを使う解法


---

そもそも、builtinに専用の関数がある
https://docs.python.org/ja/3/library/stdtypes.html#int.bit_count



> https://github.com/rihib/leetcode/pull/46#pullrequestreview-2381278969

勉強になる。特に以下。
> ここで注目したいのは、 xとその２の補数はお互いにRightmost set bit以外が反転しているということである。つまり、x & -xとすると、Rightmost set bitのみが1になったビット列を得ることができる。よって、x - (x & -x)としてあげれば、 xのRightmost set bitをunsetすることができるのである。

> Rightmost unset bitをsetする方法
flippedで考えて最後にflippする

https://www.geeksforgeeks.org/dsa/set-rightmost-unset-bit/

