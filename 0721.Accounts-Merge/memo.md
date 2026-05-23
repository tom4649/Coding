# 721. Accounts Merge

## step1
40m ぐらいかかった。UnionFindは記憶に自信がなく少し調べてしまった。
同値類を管理するデータ構造としてこれが素直な方針だと個人的には思った

revised: 変数名を改善


## 他の人のコード
https://github.com/huyfififi/coding-challenges/pull/48

```python
for i, (_, *emails) in enumerate(accounts):
```
この書き方は知らなかった。

https://peps.python.org/pep-3132/

> This PEP proposes a change to iterable unpacking syntax, allowing to specify a “catch-all” name which will be assigned a list of all items not assigned to a “regular” name.

```python
[accounts[i][0]] + sorted(emails)
```
より
```python
[accounts[i][0], *sorted(emails)]
```
の方がlistの生成回数が少ない

自分はnameで分離した後にunion-findで同値類を求めたがnameで分離しない方が自然だな。

DFSでも書ける、なるほど。

## step2
DFSとunion findで書き直し

時間計算量：

N = accounts数、E = 全email出現回数、U = ユニークemail数

DFS: O(E+UlogU)

UnionFind: O(E\alpha(N)+UlogU) \alpha: 逆アッカーマン関数


