# 650. 2 Keys Keyboard

ナップザックDPの問題から選んだ。

まず基本的なナップザック問題の復習から：

> 容量 $W$ のナップサックがあります。 $n$ 個のアイテムがあり、各アイテム $i$ には重さ $weight[i]$ と価値 $value[i]$ が設定されています。 ナップサックの総重量が $W$ を超えないようにアイテムを選んだとき、得られる価値の最大値を求めてください。

dp[i][w] = 「最初の $i$ 個のアイテムだけを使い、制限重量が $w$ であるときの価値の最大値」

として解く。

```python
def knapsack_01_2d(W: int, weights: list[int], values: list[int]) -> int:
    n = len(weights)
    # dp[i][w] のテーブルを初期化 (行: アイテム数+1, 列: 容量+1)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        w_item = weights[i - 1]
        v_item = values[i - 1]
        for w in range(W + 1):
            if w >= w_item:
                # 「選ばない」と「選ぶ」の大きい方を取る
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - w_item] + v_item)
            else:
                # 重すぎて入れられない場合は、前の状態を引き継ぐ
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]

```

空間計算量の削減

```python
def knapsack_01_1d(W: int, weights: list[int], values: list[int]) -> int:
    n = len(weights)
    dp = [0] * (W + 1)

    for i in range(n):
        w_item = weights[i]
        v_item = values[i]
        # 逆順に回すことで、同じアイテムを2回選ぶのを防ぐ
        for w in range(W, w_item - 1, -1):
            dp[w] = max(dp[w], dp[w - w_item] + v_item)

    return dp[W]
```

考え方

1. 「アイテム（選択の対象）」は何か？
- 問題文に登場する「要素のリスト」を見つけます。
- 例：硬貨（Coin Change）、文字列（Word Break）、仕事のタスク、配列の数字。

2. 「ナップサックの容量（制限リソース）」は何か？
- 「これを超えてはいけない」「ぴったりこの値にしなければならない」という足かせを見つけます。これがDP配列の長さ（列数）になります。
- 例：目標金額、合計重量、文字列の長さ、予算。

3. 「価値（最適化したい目標）」は何か？
- 「最大化」または「最小化」したい数値を特定します。これがDPの各マスに保存される値です。
- 例：総価値の最大化、使う枚数の最小化、組み合わせの総数。

応用

完全ナップサック問題 (Unbounded Knapsack)
- 特徴: 同じアイテムを何回でも選んでよい。

部分和問題 (Subset Sum / Partition Equal Subset Sum)
- 特徴: 「価値」という概念がなく、「特定の合計値を作れるか？」というYES/NOを判定する。

## step1

この問題もCopyかPasteかを選択する点がナップザックDPと似ている

ナップザックDPの考え方で解いてみる。が、かなり遅い。O(n^2)なので改善できそう。

コピーしている個数が多いほどpasteの回数は少なくなるに決まっているのでこれを利用できる。

またコピーするのは得たい文字数の約数に限られる。


## step2

https://leetcode.com/problems/2-keys-keyboard/solutions/8290642/2-keys-keyboard-prime-factorization-by-s-6zj7/?envType=problem-list-v2&envId=50vif4uc

O(\sqrt{n})まで落とせるのか。思いつかなかった。

文字数をX倍しようとするとき、X回の操作（copy1回 + pasetX-1回）が必要となる。

すると、最小回数は素因数の和に等しくなる、ということか。

この素因数分解の方法自体も覚えておこう。
