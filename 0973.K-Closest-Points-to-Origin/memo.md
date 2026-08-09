# 973. K Closest Points to Origin

## step1

まずheapを使った解法。7mほど。

n = len(points)として

時間計算量: O(n+klog n)、空間計算量: O(n)

他の解法として、ソートを思いつく。

時間計算量: O(nlogn)、空間計算量 O(k) (in-placeならO(1))

## step2

Solution の Topic、Quick select を見てもう一つの解法に気づく。

時間計算量: 平均O(n)、最悪O(n^2)、空間計算量: O(1)

partitionの実装方法に自信がなくwikipediaを見た

https://ja.wikipedia.org/wiki/%E3%82%AF%E3%82%A4%E3%83%83%E3%82%AF%E3%82%BB%E3%83%AC%E3%82%AF%E3%83%88


https://github.com/huyfififi/coding-challenges/pull/28/changes#diff-ab6bba3ca897c3d2d653f49bad85d2a075662bc1eba6f421b9689a7e80aa58f9

ヒープの使い方が異なる。こちらは時間計算量O(nlogk)、空間計算量O(k)

pointsを書き換えない場合に最も省メモリ。

> どちらにせよ必要な処理を条件分岐から出すことで、若干私の脳への収まりがよくなったが、どちらの方が人気だろう。

heappushpopは知らなかった

https://docs.python.org/3/library/heapq.html#heapq.heappushpop

一度heappushをしてから条件分岐をするかどうかについて。個人的にはメソッドとなっているheappushpopを使う方効率的なので良いと思う。heapの順序入れ替えの操作が一度で済む。

heapq.nsmallest()を使う解法

```python
import heapq


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        return heapq.nsmallest(k, points, key=lambda p: pow(p[0], 2) + pow(p[1], 2))
```

> pow() 関数を呼び出すより、　step2 のように、　x * x + y * y としたほうが読みやすく、処理が軽そうなイメージがあります。ただ、処理の重さ軽さについては、 Python のインタープリター自体が重いため、あまり気にしなくても良いかもしれません。


disライブラリというものがあるらしい。disassemblerのライブラリ。自分でも触ってみる。

https://docs.python.org/ja/3/library/dis.html

```python
def pow(a, b):
    "Same as a ** b."
    return a ** b
```

```text
# x * x
  4           0 RESUME                   0

  5           2 LOAD_FAST                0 (x)
              4 LOAD_FAST                0 (x)
              6 BINARY_OP                5 (*)
             10 RETURN_VALUE

# x**2
  8           0 RESUME                   0

  9           2 LOAD_FAST                0 (x)
              4 LOAD_CONST               1 (2)
              6 BINARY_OP                8 (**)
             10 RETURN_VALUE

# pow(x, 2)
 12           0 RESUME                   0

 13           2 LOAD_GLOBAL              1 (NULL + pow)
             12 LOAD_FAST                0 (x)
             14 LOAD_CONST               1 (2)
             16 CALL                     2
             24 RETURN_VALUE
```

これを見ても x * xが良さそう

## その他

https://github.com/ryosuketc/leetcode_grind75/pull/28


https://github.com/naoto-iwase/leetcode/pull/74/changes

「YAGNI」という知らない用語があった。

> 「YAGNI（ヤグニ）」とは、ソフトウェア開発における非常に有名な原則（設計思想）の一つで、「You Aren't Gonna Need It（どうせそれ、必要にならないよ）」の頭文字を取ったもの

https://ja.wikipedia.org/wiki/YAGNI



## step3

クイックセレクトに馴染みがないのでこれを練習する。
