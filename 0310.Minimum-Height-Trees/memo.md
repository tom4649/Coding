# 310. Minimum Height Trees

## step1

30mぐらい考えたが解けなかった

> hint: How many MHTs can a graph have at most?

AIに聞いてみる: 木の葉を一つずつ削っていくことを考えると最後に残るのノードはひとつか二つでこれが答え

何となく正しそうなので、厳密に証明できていないがこれを実装してみる: step1.py
- 時間計算量: O(n)
- 空間計算量: O(n)


## step2

変数名などを少し改善

木の中心を求めるアルゴリズムとして証明されている

https://inzkyk.xyz/graph/tree-and-arborescence/centers-of-graph-and-tree/

### 他の人のコード

https://github.com/huyfififi/coding-challenges/pull/63/changes

木を2回探索すれば直径を求めることができる

https://algo-logic.info/tree-diameter/

https://sasanquaneuf.github.io/math-toybox/apps/cs_mht.html

分かりやすい

木の高さを最小にする頂点は一つか二つであることとも合わせると、一つのパスを求めてそのパスの中心（一つか二つ）を求めれば良いことになる

## step3
上を実装


- 時間計算量: O(n)
- 空間計算量: O(n)
