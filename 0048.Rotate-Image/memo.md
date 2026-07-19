# 48. Rotate Image

## step1
転置と反転でかける。4mぐらい。

転置と反転が二面体群d4の生成元であることから従う。

エラー処理を少しだけ変える。

## 他の人のコード

https://github.com/potrue/leetcode/pull/80

setを使った解法。メモリをO(n^2)使っているので二次元配列をもう一つ使う解法と変わらないのでは。

> matrix[y][x] となると思います

この順番はたまに目にする

https://leetcode.com/problems/rotate-image/solutions/8136968/rotate-image-sol-in-py-by-aryankumardube-8gti/

外部メモリを使って良いなら一行で書ける

```python
matrix[::]=[list(reversed(col)) for col in zip(*matrix)]
```

https://leetcode.com/problems/rotate-image/solutions/8134901/cyclic-orbit-permutation-by-mpractice-sfyq/

matrixを一度しか触らない方法もある。インデックスがややこしい。
