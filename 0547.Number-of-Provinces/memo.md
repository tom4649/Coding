# 547. Number of Provinces

## step1
14mほど。タイプミス以外ミスなくかけた。UnionFindの基本問題。

## step2
改善

path compression + Union by size

---


```python
# ① Path Compression（経路圧縮）
def find_compression(self, x: int) -> int:
    if self.parent[x] != x:
        self.parent[x] = self.find_compression(self.parent[x])  # 根に直結
    return self.parent[x]

# ② Path Splitting（経路分割：ループ版・通った全ノードを祖父母へ繋ぐ）
def find_splitting(self, x: int) -> int:
    while x != self.parent[x]:
        # 親を「祖父母」に書き換えつつ、自分は元の「親」へ進む
        self.parent[x], x = self.parent[self.parent[x]], self.parent[x]
    return x

# ③ Path Halving（経路半減：ループ版・1つおきに祖父母へ繋ぐ）
def find_halving(self, x: int) -> int:
    while x != self.parent[x]:
        self.parent[x] = self.parent[self.parent[x]]  # 親を「祖父母」に書き換え
        x = self.parent[x]  # 書き換えた「祖父母」へ一気にジャンプ
    return x
```

```python
# ① Union by Size（要素数で比較：実務・面接で一番おすすめ）
class UnionFindBySize:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n  # 最初は全員サイズ1

    def union(self, x: int, y: int) -> bool:
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.size[rx] > self.size[ry]:  # rx を小さい方にする
            rx, ry = ry, rx
        self.parent[rx] = ry
        self.size[ry] += self.size[rx]  # 要素数を合算
        return True


# ② Union by Rank（高さの目安で比較）
class UnionFindByRank:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n  # 最初は全員高さ0

    def union(self, x: int, y: int) -> bool:
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] > self.rank[ry]:  # rx を低い方にする
            rx, ry = ry, rx
        self.parent[rx] = ry
        if self.rank[rx] == self.rank[ry]:  # 高さが同じ時だけ +1
            self.rank[ry] += 1
        return True
```

これらのいずれかを組み合わせると計算量は逆アッカーマン関数になる

https://ja.wikipedia.org/wiki/%E7%B4%A0%E9%9B%86%E5%90%88%E3%83%87%E3%83%BC%E3%82%BF%E6%A7%8B%E9%80%A0
