# 155. Min Stack

## step1

はじめにヒープが頭に浮かんだが、最小値の更新にO(logn)かかる
もっと単純に考えた: step1.py
15mぐらいかかった

## step2

pushを変更

getMinやpopのエラー処理はNoneを返す処理に変えることも考えたが、LeetCodeの返り値に合わせてこのままにした

### 他の回答
- https://hayapenguin.com/notes/LeetCode/155/MinStack

最小値が更新される同じ値のときだけmin_stackに追加する方法

順序が単調なスタックをMonotonic Stackというらしい

- https://github.com/Exzrgs/LeetCode/pull/35

同じ解法

- https://github.com/huyfififi/coding-challenges/pull/38/changes

スタックを2本持つ代わりに、(値, その時点での最小値) のタプルを1本のスタックで管理する。

```python
self.num_and_prefix_min = []  # [(val, prefix_min), ...]

def push(self, val):
    if not self.num_and_prefix_min:
        self.num_and_prefix_min.append((val, val))
    else:
        prev_min = self.getMin()
        self.num_and_prefix_min.append((val, min(val, prev_min)))

def top(self):
    return self.num_and_prefix_min[-1][0]  # タプルの1要素目

def getMin(self):
    return self.num_and_prefix_min[-1][1]  # タプルの2要素目
```

自分の解法と本質的には同じだが、
1本にまとめることで `top` と `getMin` が常にセットで扱われることが明示的になる。
`prefix_min` という命名は「そのpushまでの最小値」を表す。

### Monotonic Stack（単調スタック）

スタック内の要素が常に単調増加 or 単調減少になるように維持するデータ構造。

**単調減少スタック（Monotone Decreasing Stack）の例:**
- pushするとき、新しい要素より小さい要素をpopしてから積む
- 結果としてスタックは上から下に向かって単調増加（= 底が最小値）

このMin Stackで使われている `min_data` も一種の単調スタック:
- `min_data[-1]` が常に現時点での最小値
- pushのたびに `min(現在の最小値, 新しい値)` を積むことで単調非増加を維持

**使われる典型問題:**
- 次に大きい/小さい要素を求める（Next Greater Element）
- ヒストグラムの最大面積
- 雨水の溜まる量（Trapping Rain Water）

これらはO(n²)の全探索をO(n)に落とせる。

後で解く:

https://leetcode.com/problems/next-greater-element-i/description/

https://x.com/sakamoto_582/status/1808159283852595531

## step3
書くことには問題がないので省略
